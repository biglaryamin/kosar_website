from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="presentation_blog"
urlpatterns=[
    path('', views.show_main_page, name='main_page'),
    path('services', views.show_services, name='services'),
    path('detail-services', views.show_services_detail, name='service-detail'),
    path('shop', views.show_shop, name='shop'),
    path('detail-shop', views.show_shop_detail, name='shop-detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)