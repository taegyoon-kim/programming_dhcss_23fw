# -*- coding: utf-8 -*-
"""programming_dhcss_exercise_w11_exercise

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1za4F40L4r5epqWh00YMaYOjsuYxWPxuB

### Art Institute of Chicago API

Import the requests module.
"""

import requests

"""Create a URL that searches for the works of Monet in the Art Institute of Chicago."""

# we can access the /artworks listing endpoint to see all of the published artworks in the AIC's collection
API_base_url = 'https://api.artic.edu/api/v1/artworks/search?'

# creat a query string
search_url = API_base_url + 'q=monet'
print(search_url)

# get will send a GET request to any web page
r = requests.get(search_url)

"""`print()` will print the response code. There are five types of response codes:

- 1xx informational response – the request was received, continuing process
- 2xx successful – the request was successfully received, understood, and accepted
- 3xx redirection – further action needs to be taken in order to complete the request
- 4xx client error – the request contains bad syntax or cannot be fulfilled
- 5xx server error – the server failed to fulfil an apparently valid request

**Most common:** 200 (success) or 4xx (something wrong with request)


"""

print(type(r))
print(r.status_code)

"""Another approach is to use the `params` argument in `requests.get()`. Simply provide a dictionary of `key:value` pairs that will be the parameters."""

r = requests.get(API_base_url, params = {"q": "monet"})

"""`.text` attribute will return the text that was received from the server. This API automatically returns a string in JSON format."""

print(type(r.text))
print(r.text)

"""We could turn it into a dictionary using the `json` module."""

import json
r_dict = json.loads(r.text)

"""A more direct way would be to use the `.json()` method:"""

r_dict = r.json()
r_dict

"""What are its keys?"""

r_dict.keys()

"""Check the keys. There is some useful info in `pagination`."""

r_dict['pagination']

r_dict['data']

"""`r_dict['data']` gave us a list. Let's make sure:"""

type(r_dict['data'])

"""Check out the length of the list:"""

len(r_dict['data'])

"""Check out just one item from the list:"""

r_dict['data'][0]

"""We can use the given api link to make an API request about this specific work:"""

res = requests.get(r_dict['data'][0]['api_link']).json()
res

"""Get information about height in cm, weight in cm, and medium"""

res.keys()

res['data'].keys()

res['data']['dimensions_detail'] # notice that this a list of length 1!

res['data']['dimensions_detail'][0]['height_cm']
res['data']['dimensions_detail'][0]['width_cm']

"""Get the medium too:"""

res['data']['medium_display']

"""After the exploration, let's work to get:

- title
- id
- height_cm
- width_cm


Use search endpoint to get the API links to works of 'Monet', then use those links to get the rest.

We had seen that there were 296 works in total.
"""

r_dict['pagination']

"""Can we request them all?"""

r_new = requests.get(API_base_url, params = {"q": "Monet", 'size': 296})
r_new

r_new.text

r_new.status_code

r_dict['pagination']

"""The documentation says "For performance reasons, limit cannot exceed 100." So, let's request 50 records each time"""

from time import sleep

size = 50
container = []
current_page = 0
total_pages = 1
from_ = 0
while current_page < total_pages:
    r = requests.get(API_base_url, params = {"q": "Monet", 'size': size, 'from': from_})
    assert r.status_code == 200 # raiases an AssertionError is the condition is not satisfied
    r_dict = r.json()
    print('Number of results from this iteration is', str(len(r_dict['data'])))
    container.extend(r_dict['data']) # not append
    current_page = r_dict['pagination']['current_page']
    print('Current page is', current_page)
    total_pages = r_dict['pagination']['total_pages']
    print(str(current_page) + ' of ' + str(total_pages) + ' completed!\n')
    from_ = from_ + size
    sleep(3)

len(container)

container[0]

container[0]['thumbnail']['alt_text']

"""Use list comprehension to only get the information we care about (a list where every item is a dictionary)"""

container2 = [{'id' : item['id'], 'api_link' : item['api_link'], 'title': item['title']} for item in container]

container2

"""If we wanted the alt_text too, we would get the following error because some items apparently don't have an 'alt_text'. Then we would need to devise a strategy to deal with it."""

container3 = [(item['id'], item['api_link'], item['title'], item['thumbnail']['alt_text']) for item in container]

container3 = []
for item in container:
    try:
        container3.append({'id': item['id'], 'api_link': item['api_link'], 'title': item['title'], 'alt_text': item['thumbnail']['alt_text']})
    except:
        container3.append({'id': item['id'], 'api_link': item['api_link'], 'title': item['title'], 'alt_text': None})