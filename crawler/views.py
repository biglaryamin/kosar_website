# regex
import re

# django
from django.shortcuts import render, HttpResponse
from .models import CrawledArticle

# For crawling data
import requests
from bs4 import BeautifulSoup

# importing task from tasks.py file  
from .tasks import test_func  
    

    
def test_celery(request):  
    # call the test_function using delay, calling task  
    # test_func()  
    return HttpResponse("Done")  
 

def crawler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    titles = soup.select("tr td span.titleline")

    temp_links = soup.select("tr td span a")
    links = []
    for link in temp_links:
        try:
            temp_link = re.findall(r".*href=(.*?)\>", str(link))
            links.append(temp_link)
        except:
            pass

    return (titles, links)


def remove_extra_letter(url):
    end = len(url)-1
    result = url[2:end-1]
    return result


def test(request):
    counter = 2
    url = "https://news.ycombinator.com/"
    # get_links(url)
    links = crawler(url)[1]
    print(f"--------------{links}------------------------")
    articles = CrawledArticle.objects.all().order_by('-created')
    local_articles = []
    for article in articles:
        local_articles.append(str(article.title))
        
    for link in crawler(url)[0]:
        correct_link = remove_extra_letter(str(links[counter]))
        try:
            the_article = CrawledArticle(title=link.text, link = correct_link)
            print("works")
        except IndexError:
            the_article = CrawledArticle(title=link.text, link = "index error!")
            print("error")
        
        if str(the_article.title) not in local_articles:
            the_article.save()


        counter += 1
    
    articles = CrawledArticle.objects.all().order_by('-created')
    print(f"******* number of all articles are : {articles.count()} **********")
    return render(request, "crawler/list.html", {"articles":articles})