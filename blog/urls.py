from django.urls import path,include
from .views import ArticleList,CategoryList,AuthorList
from .views import show_article_detail,show_contact_page,show_base_page
from . import views

#api
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

from .views import test_ajax

app_name="blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('contact', show_contact_page , name="contact"),
    path('base', show_base_page , name="base"),
    path('page/<int:page>', ArticleList.as_view(), name="home"),
    path('searched_item/', views.search , name="search_view"),
    path('article/<slug:slug>', show_article_detail , name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),

    path('test_ajax', test_ajax, name="test_ajax"),
    #api
    path('', include(router.urls)),
]