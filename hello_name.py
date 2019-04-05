import re

string = input("Hello! What is your name?\n > ")
sample_name = re.compile(r'\b[A-Z][a-z]{2,}\b')
name = sample_name.search(string)
print("Hello, {}!".format(name.group(0)))