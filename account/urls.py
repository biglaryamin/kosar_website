from django.contrib.auth import views
from django.urls import path
from .views import ArticlelList,ArticleCreate,ArticleUpdate,ArticleDelete,Profile

from django.conf.urls.static import static
from django.conf import settings

app_name="account"
urlpatterns=[
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name="article-update"),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name="article-delete"),
    path('profile', Profile.as_view(), name="profile"),


]



urlpatterns+=[
    path('', ArticlelList.as_view(), name="home"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

