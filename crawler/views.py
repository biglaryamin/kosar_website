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
    articles = CrawledArticle.objects.all().order_by('-created')
    local_articles = []
    for article in articles:
        local_articles.append(str(article.title))
        
    for link in crawler(url):
        try:
            the_article = CrawledArticle(title=link.text)
            if str(the_article.title) not in local_articles:
                the_article.save()

        except:
            pass

    author = ""
    print(f"******* number of all articles are : {articles.count()} **********")
    return render(request, "crawler/list.html", {"articles":articles, "author":author})