#!/usr/bin/python3

""" Show all countries on the site page.
"""

import html
from urllib.request import urlopen, Request

SITE_URL = "http://example.webscraping.com/"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
site_request = Request(SITE_URL, headers = headers)
site_page = urlopen(site_request).read()
site_page = str(site_page)


COUNTRY_TAG = 'png" /> '


while COUNTRY_TAG in site_page:
	
	country_tag_size = len(COUNTRY_TAG)
	country_tag_index = site_page.find(COUNTRY_TAG)
	country_value_start = country_tag_index + country_tag_size
	country = ''
	for char in site_page[country_value_start:]:
		if char != '<':
			country += char
		else:
			break
	print(country)
	site_page = site_page[country_value_start:]

