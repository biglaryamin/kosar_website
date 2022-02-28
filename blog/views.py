from django.shortcuts import render


def show_articles(request):
    return render(request,'blog/list_view.html')