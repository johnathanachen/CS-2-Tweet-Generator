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

source_text = get_transcript_html()

def _get_words(source_text):
    word_list = []
    for sentence in source_text:
        word_list.append(sentence.split(' '))
    combined_word_list = [inner for outer in word_list for inner in outer]
    remove_unicode = [word.strip('\xa0') for word in combined_word_list]
    for word in remove_unicode:
        if "</i>" in word:
            remove_unicode.remove(word)
    for word in remove_unicode:
        if "<i>" in word:
            remove_unicode.remove(word)
    return remove_unicode

only_words = _get_words(source_text)

def histrogram(only_words):
    word_count = []
    added_words = []
    tuple_list = []

    for word in only_words:
        if word in added_words:
            new_count = arr_word
            arr_word[1] += 1
        else:
            arr_word = [word]
            word_count.append(arr_word)
            added_words.append(word)
            arr_word.append(1)

    for word in word_count:
        tuple_list.append(tuple(word))

    return tuple_list

tuples = histrogram(only_words)

def save_to_txt(tuples):
    with open ('tuple_to_text.txt','w') as f:
        for i in tuples:
            f.write(str(i) + '\n')

save_to_txt(tuples)
