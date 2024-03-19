import requests
from bs4 import BeautifulSoup 


target_url = "https://news.ycombinator.com"
found_links = []
def make_request(url):
    get_url = requests.get(url)
    soup = BeautifulSoup(get_url.text, "html.parser")
    return soup


def news(url):
    links = make_request(url)
    i = 1
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "https://" in found_link: 
                if found_links not in found_links:
                    found_links.append(found_link)
                    print(i , "- " , found_link)
                    i += 1
            if len(found_links) == 30:
                break

news(target_url)