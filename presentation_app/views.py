from django.shortcuts import render,HttpResponse


def show_main_page(request):
    return render(request,"presentation_blog/index.html")