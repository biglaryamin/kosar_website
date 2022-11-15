from celery import shared_task  
    


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




@shared_task()  
def test_func():  
    url = "https://news.ycombinator.com/"
    links = crawler(url)[1]

    print("------------------hello there----------------")