from django.urls import path
from django.conf.urls import url
from das_app import views

app_name = "das_app"

urlpatterns = [
    path("list/", views.SchoolList.as_view(), name="list"),
    # path("details/", views.SchoolDetail.as_view(), name="detail"),
    # url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetail.as_view(), name="detail"),
    path("list/<pk>/", views.SchoolDetail.as_view(), name="detail"),
    path("create/", views.SchoolCreateView.as_view(), name="create"),
    path("update/<pk>/", views.SchoolUpdateView.as_view(), name="update"),
    path("delete/<pk>/", views.SchoolDeleteView.as_view(), name="delete"),
]
