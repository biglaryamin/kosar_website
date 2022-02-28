from django.urls import path,include
from . import views

urlpatterns = [
    path("list_articles" , views.show_articles , name="show_articles"),
]


