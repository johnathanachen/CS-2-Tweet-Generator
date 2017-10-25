from pathlib import Path
import re

sample_text = Path("sample_text.txt")
f = open("sample_text.txt")

def file_arr():
    file_arr = []
    for text in f:
        file_arr.append(text)

    return file_arr

file_arr = file_arr()

def freq(file_arr):
    for text in file_arr:
        morty_strs = re.search("(?<=Morty: )", text)
        print(morty_strs.group(0))

freq(file_arr)
