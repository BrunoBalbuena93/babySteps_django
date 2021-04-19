from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as gen
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Lista de los post relacionados con el usuario y/o grupo
class PostList(SelectRelatedMixin, gen.ListView):
    model = models.Post
    select_related = ("user", "group")
    
    
# View para los posts del usuario en turno
class UserPosts(gen.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"
    
    # Busca exactamente los posts del usuario que se está utilizando
    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    
    # Similar al queryset, sirve para jalar los posts del usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context



class PostDetail(SelectRelatedMixin, gen.DetailView):
    model = models.Post
    select_related = ("user", "group")
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, gen.CreateView):
    fields = ("message", "group")
    model = models.Post
    
    def form_valid(self, form):
       self.object = form.save(commit=False) 
       self.object.user = self.request.user
       self.object.save()
       return super().form_valid(form)
   

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, gen.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)
    
    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post deleted")
        return super().delete(*args, **kwargs)