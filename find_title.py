#!/usr/bin/env python

import re
from bs4 import BeautifulSoup
from pathlib import Path

folder = 'program'
folder2 = '6'
file = 'SINOPTIK.html'

file_path = Path.home() / folder / folder2 / file
if file_path.exists():
	with (file_path).open('r') as f:
		text_html = f.read()
		page = BeautifulSoup(text_html, 'html.parser')
		for title in page.find_all('title'):
			print(title.text)






                        

