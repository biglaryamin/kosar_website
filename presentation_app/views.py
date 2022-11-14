from django.shortcuts import render,HttpResponse

from .models import ImageModel, TextModel

def show_main_page(request):
    first_wallpaper = ImageModel.objects.get(name="wallpaper1")
    second_wallpaper = ImageModel.objects.get(name="wallpaper2")
    all_text = TextModel.objects.all()
    main_text = all_text[0]
    second_text = all_text[1]
    return render(request,"presentation_blog/index.html", {"first_wallpaper":first_wallpaper,
                                                            "second_wallpaper":second_wallpaper,
                                                            "main_text":main_text,
                                                            "second_text":second_text})


def show_services(request):
    return render(request , 'presentation_blog/services.html')


def show_services_detail(request):
	return render(request , "presentation_blog/services-details.html")


def show_shop(request):
    return render(request,"presentation_blog/shop.html")


def show_shop_detail(request):
    return render(request,"presentation_blog/shop-details.html")
