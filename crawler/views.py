from django.shortcuts import render, HttpResponse
from .models import CrawledArticle

# For crawling data
import requests
from bs4 import BeautifulSoup


def crawler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.select("tr td span.titleline")
    return links


def test(request):
    url = "https://news.ycombinator.com/"

    for link in crawler(url):
        try:
            the_article = CrawledArticle(title=link.text)
            the_article.save()
        except:
            the_article = CrawledArticle(title="can not save")
            the_article.save()

    articles = CrawledArticle.objects.all()
    author = ""
    return render(request, "crawler/list.html", {"articles":articles, "author":author})