from django.urls import path

from .import views

app_name= "relocation"
urlpatterns = [
    path('', views.home, name='home'),
    path("detail", views.detail, name="detail")
    #path('', ProspectCreateView.as_view(), name='home')
]