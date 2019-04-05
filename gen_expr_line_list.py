#!/usr/bin/python3

import os
from pathlib import Path


dir=os.path.abspath(os.curdir)

print(f'Your current directory is : {dir}\n')
print("List of first lines of all files in the current directory:\n")

gen_expr = (os.path.join(r,file) for r, d, f in os.walk(os.getcwd()) for file in f)

for files in gen_expr:
	try:
		for line in open(files):
			print(line)
			break
	except UnicodeDecodeError:
		for line in open(files, 'rb'):
			print(line)
			break










