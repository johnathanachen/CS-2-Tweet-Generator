import bs4 as bs
from urllib.request import urlopen
import re

def get_transcript_html():
    transcript_url = 'http://rickandmorty.wikia.com/wiki/Pilot/Transcript'
    transcript_url_request = urlopen(transcript_url)
    transcript_html = transcript_url_request.read()
    transcript_html = transcript_html.decode('utf-8')

    x = bs.BeautifulSoup(transcript_html, "lxml").find_all('div', attrs={"class":"poem"})

    print(x)
    # list_html = transcript_html.split('price')


get_transcript_html()
# def freq(file_arr):
#     for text in file_arr:
#         morty_strs = re.search("(?<=Morty: )", text)
#         print(morty_strs.group(0))
#
# freq(file_arr)
