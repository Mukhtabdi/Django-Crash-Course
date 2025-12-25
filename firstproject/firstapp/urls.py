from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloSomalia.as_view()),
]