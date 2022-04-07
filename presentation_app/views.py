from django.shortcuts import render,HttpResponse


def show_main_page(request):
    return render(request,"presentation_blog/index.html")


def show_services(request):
    return render(request , 'presentation_blog/services.html')


def show_services_detail(request):
	return render(request , "presentation_blog/services-details.html")



def show_shop(request):
    return render(request,"presentation_blog/shop.html")


def show_shop_detail(request):
    return render(request,"presentation_blog/shop-details.html")
