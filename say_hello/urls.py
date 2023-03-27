from django.urls import path
from . import views


urlpatterns = [
    path('' , views.SayHello.as_view() , name='just_say_hello')
]