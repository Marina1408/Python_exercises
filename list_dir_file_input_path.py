#!/usr/bin/python3

"""This program find all files and directories in the directory,
   which is entered by the user.
"""

from pathlib import Path


c = input("Input the path in the format /_/_ : \n")
p = Path(c)
lst = [f for f in p.iterdir() if f.is_dir() or f.is_file()]
print(lst)


