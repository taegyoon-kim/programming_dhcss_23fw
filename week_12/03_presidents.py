# -*- coding: utf-8 -*-
"""03_presidents.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wcIqcW03Qzj8YbCSGhIFBSfz-t0BOWpF

### **Getting Portrait and Early Life Information for All U.S. Presidents from Wikipedia**

Get the Wikipedia links to all U.S. presidents. The page https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States has them, we need to extract it.
"""

from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
soup = BeautifulSoup(r.text)

print(soup.find(class_ = 'wikitable').prettify())

[item for item in soup.find(class_ = 'wikitable').tbody.find_all('tr')][10].find_all('td')[1].a.get('href')

links = []
for item in soup.find(class_ = 'wikitable').tbody.find_all('tr'):
    try:
      links.append('https://en.wikipedia.org' + item.find_all('td')[1].a.get('href'))
    except:
      None

links

len(links)

def get_early_life(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    heading = [item for item in soup.find_all(['h2','h3']) if 'early life' in item.text.lower()]
    first_paragraph = heading[0].find_next('p').text
    return first_paragraph

def get_portrait(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.text)
    infobox_image = soup.find(class_ = 'infobox-image')
    url = 'https:' + infobox_image.img.get('src')
    return url

i = 0
container_dict = {}
for link in links:
    i += 1
    print(i)
    new_dict = {}
    # turns out, Abraham Lincoln's 'early life' section was designed differently than everyone else
    # so we'll circumvent that with try / except
    try:
        new_dict['early_life'] = get_early_life(link)
    except:
        new_dict['early_life'] = None
    new_dict['portrait'] = get_portrait(link)
    container_dict[link.replace('https://en.wikipedia.org/wiki/', '')] = new_dict

container_dict