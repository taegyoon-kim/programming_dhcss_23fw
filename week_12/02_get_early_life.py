# -*- coding: utf-8 -*-
"""02_get_early_life.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13f1LAVIXcGTDoV5K-5TX_3TYTQNRlcME

### **Getting Early Life Information for U.S. Presidents from Wikipedia**

Information on the early life of all U.S. presidents. Let's take the **first paragraph** that discusses the early life of U.S. presidents.

Take a look at some of their pages to decide how we can target them:

https://en.wikipedia.org/wiki/William_McKinley

https://en.wikipedia.org/wiki/John_Adams

https://en.wikipedia.org/wiki/Thomas_Jefferson

It's somewhat difficult to exactly target that portion of the page:

- There are many paragraphs, if we target all paragraphs, we need a way to distinguish between the scraped paragraphs
- We can try to look at the paragraph in the "Early life" section---but this section is named differently each time ("Early life and education", "Early life and career", "Early life and family")
- Subsection headings always has a `h` tag and a `mw-headline` class---but all subsections have it
- My approach is to look through section headings and take the one that has the phrase "early life" somewhere
"""

from bs4 import BeautifulSoup
import requests

"""Let's do for one page first: https://en.wikipedia.org/wiki/George_Washington"""

url = 'https://en.wikipedia.org/wiki/George_Washington'
r = requests.get(url)
soup = BeautifulSoup(r.text)

r.status_code

soup.find_all(['h2','h3'])

"""List comprehension: what text appears under each h2 tag?"""

[item.text for item in soup.find_all('h2')]

"""Our target is the second heading! (Index 1). We could target it even more."""

heading = [item for item in soup.find_all('h2') if 'early life' in item.text.lower()]
type(heading)
heading[0]

"""Use the find_next function to identify a next `p` tag"""

first_paragraph = heading[0].find_next('p').text

"""Put all these into a function."""

def get_early_life(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    heading = [item for item in soup.find_all(['h2','h3']) if 'early life' in item.text.lower()]
    first_paragraph = heading[0].find_next('p').text
    return first_paragraph

"""Try on a different article to see if it works:"""

url = 'https://en.wikipedia.org/wiki/William_McKinley'
get_early_life(url)

