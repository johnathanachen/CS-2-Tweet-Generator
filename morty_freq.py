import bs4 as bs
from urllib.request import urlopen
import re

def get_transcript_html():
    transcript_url = 'http://rickandmorty.wikia.com/wiki/Pilot/Transcript'
    transcript_url_request = urlopen(transcript_url)
    transcript_html = transcript_url_request.read()
    transcript_html = transcript_html.decode('utf-8')
    transcript_list = bs.BeautifulSoup(transcript_html, "lxml").find_all('div', attrs={"class":"poem"})
    dialouge_list = re.findall( '<b>Morty:</b>(.*?)<br/>', str(transcript_list), re.DOTALL)
    return dialouge_list

def histrogram(dialouge_list):


    # print(transcript_list)
    # list_html = transcript_html.split('price')

    # <b>Morty:</b> *rubs his eyes* What, Rick? What’s going on?<br/>

get_transcript_html()
