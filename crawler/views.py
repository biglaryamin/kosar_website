# django
from django.shortcuts import render
from .models import CrawledArticle


def test(request):
    articles = CrawledArticle.objects.all().order_by('-created')
    return render(request, "crawler/list.html", {"articles":articles})