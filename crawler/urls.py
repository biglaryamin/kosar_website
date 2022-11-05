from django.urls import path
from .views import test

app_name="crawler"
urlpatterns=[
    path('test', test_view, name='test'),
]



