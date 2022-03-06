from django.urls import path,include
from .views import home,create,vote,results


app_name="poll"
urlpatterns = [
path('home', home, name='home'),
path('create/', create, name='create'),
path('vote/<poll_id>/', vote, name='vote'),
path('results/<poll_id>/', results, name='results'),
]
