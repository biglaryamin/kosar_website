from django.shortcuts import render, HttpResponse
from .models import CrawledArticle


def test(request):
    articles = CrawledArticle.objects.all()
    return render(request, "crawler/list.html", {"articles":articles})