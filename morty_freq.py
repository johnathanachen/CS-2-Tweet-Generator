from pathlib import Path
import bs4 as bs
import re

sample_text = Path("sample_text.txt")
f = open("sample_text.txt")

def freq():
    list_thing = []
    for text in f:
        x = re.search('Morty:*', text)
    print(x)
    # print(list_thing)
        



freq()
