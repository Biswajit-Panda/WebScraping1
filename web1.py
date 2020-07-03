import requests
from bs4 import BeautifulSoup

page = requests.get('https://pythonprogramming.net/')
soup = BeautifulSoup(page.content, 'html.parser')
title_class = soup.find_all(class_='card-title')
content_class = soup.find_all(class_='card-content')

content = [content_class[i].find().get_text() for i in range(len(content_class))]
heading = [title_class[i].find().get_text() for i in range(len(title_class))]

print(heading)
print(content)
#print(heading)
