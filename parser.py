import requests
from bs4 import BeautifulSoup

def getNews():
    req = requests.get("https://www.vedomosti.ru/rss/rubric/lifestyle/culture.xml").content
    soup = BeautifulSoup(req, 'html.parser')

    elements = []

    for i in soup.find_all('item'):
        title = i.find('title').text
        description = i.find('description').text
        link = i.find('guid').text

        elements.append([title, description, link])

    return elements
