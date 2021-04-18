from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_home, name='home'),
    path('about', views.page_about, name="about")
]