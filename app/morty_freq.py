from pathlib import Path
import re

sample_text = Path("sample_text.txt")
f = open("sample_text.txt")

def freq():
    for text in f:
        print(text)

>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
