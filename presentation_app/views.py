from django.shortcuts import render,HttpResponse

from .models import ImageModel

def show_main_page(request):
    # the_image = ImageModel.objects.get(name="wallpaper3")
    the_image = ImageModel.objects.get(id=123)
    return render(request,"presentation_blog/index.html", {"the_image":the_image})


def show_services(request):
    return render(request , 'presentation_blog/services.html')


def show_services_detail(request):
	return render(request , "presentation_blog/services-details.html")



def show_shop(request):
    return render(request,"presentation_blog/shop.html")


def show_shop_detail(request):
    return render(request,"presentation_blog/shop-details.html")
