from django.shortcuts import render,HttpResponse

from .models import ImageModel

def show_main_page(request):
    first_wallpaper = ImageModel.objects.get(name="wallpaper1")
    second_wallpaper = ImageModel.objects.get(name="wallpaper2")
    return render(request,"presentation_blog/index.html", {"first_wallpaper":first_wallpaper,
                                                            "second_wallpaper":second_wallpaper})


def show_services(request):
    return render(request , 'presentation_blog/services.html')


def show_services_detail(request):
	return render(request , "presentation_blog/services-details.html")



def show_shop(request):
    return render(request,"presentation_blog/shop.html")


def show_shop_detail(request):
    return render(request,"presentation_blog/shop-details.html")
