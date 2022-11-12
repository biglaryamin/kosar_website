from django.urls import path
from .views import test, test_celery

app_name="crawler"
urlpatterns=[
    path('test', test, name='test'),
    # celery
    path('test_celery', test_celery, name='test_celery'),
]



