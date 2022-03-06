from django.urls import path
from . import views

app_name="presentation_blog"
urlpatterns=[
    path('main_page', views.show_main_page, name='main_page'),
]