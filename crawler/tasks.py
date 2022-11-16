# python packages
import requests
import re

# python 
from .models import CrawledArticle

# 3rd party packages
from celery import shared_task  
from bs4 import BeautifulSoup


def crawler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    titles = soup.select("tr td span.titleline")
    temp_links = soup.select("tr td span a")
    links = []
    sources = []
    for link in temp_links:
        try:
            temp_link = re.findall(r".*href=(.*?)\>", str(link))
            links.append(temp_link)
            print(link)
            temp_source = re.findall(r".*\((.*\..*)\)", str(link))
            sources.append(temp_source)

        except:
            pass


    # for source in sources:
    #     print(source)
    #     print("********************************")
    return (titles, links)


def remove_extra_letter(url):
    end = len(url)-1
    result = url[2:end-1]
    return result


@shared_task()  
def test_func():  
    counter = 2
    url = "https://news.ycombinator.com/"
    links = crawler(url)[1]
    articles = CrawledArticle.objects.all().order_by('-created')
    local_articles = []
    for article in articles:
        local_articles.append(str(article.title))
        
    for link in crawler(url)[0]:
        correct_link = remove_extra_letter(str(links[counter]))
        try:
            the_article = CrawledArticle(title=link.text, link = correct_link)
        except IndexError:
            the_article = CrawledArticle(title=link.text, link = "index error!")
        
        if str(the_article.title) not in local_articles:
            the_article.save()

        counter += 1
    
    articles = CrawledArticle.objects.all().order_by('-created')
    print(f"******* number of all articles are : {articles.count()} **********")