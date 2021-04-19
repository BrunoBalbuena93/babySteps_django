from django.urls import path, reverse, reverse_lazy
from polls import views
app_name = "polls"
urlpatterns = [
    # Inicio
    path('', views.IndexView.as_view(), name='index'),
    # polls/<poll>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # polls/<poll>/result/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # polls/<poll>/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
]