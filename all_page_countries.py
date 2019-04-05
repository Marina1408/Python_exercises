#!/usr/bin/python3

""" Show all countries on the site page.
"""
import time
import html
from urllib.request import urlopen, Request

SITE_URL = "http://example.webscraping.com/places/default/index/00"

# getting page from server
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;)'}
site_request = Request(SITE_URL, headers = headers)
site_page = urlopen(site_request).read()
site_page = str(site_page)

NEXT_TAG = '>Next &gt;</a>'
COUNTRY_TAG = 'png" /> '
i = 0

while NEXT_TAG in site_page:
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
	i += 1	

	if i <= 10:
		SITE_URL = SITE_URL[:len(SITE_URL) - 1] + str(i)
	else:
		SITE_URL = SITE_URL[:len(SITE_URL) - 2] + str(i)

	site_request = Request(SITE_URL, headers = headers)
	time.sleep(2)
	site_page = urlopen(site_request).read()
	site_page = str(site_page)
	
