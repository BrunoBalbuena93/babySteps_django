from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic as gen
from .models import Group, GroupMember
from django.contrib import messages

class CreateGroup(LoginRequiredMixin,gen.CreateView):
    model = Group
    fields = ("name", "description")
    
    
class SingleGroup(gen.DetailView):
    model = Group
    

class ListGroups(gen.ListView):
    model = Group

class JoinGroup(gen.RedirectView, LoginRequiredMixin):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, 'Ya eres un miembro!')
        else:
            messages.success(self.request, 'Te has unido al grupo')
        return super().get(request, *args, **kwargs)
    

class LeaveGroup(LoginRequiredMixin, gen.RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get("slug")).get()
        except:
            messages.warning(self.request, 'No eres miembro')
        else:
            membership.delete()
            messages.success(self.request, 'Has abandonado el grupo')
        return super().get(request, *args, **kwargs)
    