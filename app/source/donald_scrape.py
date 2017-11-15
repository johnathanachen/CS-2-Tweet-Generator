import bs4 as bs
from urllib.request import urlopen
from string import punctuation
import re
from dictogram import print_histogram
from pathlib import Path

from dictogram import Dictogram


class Scrape():

    def __init__(self):
        self = self.scrape()

    def _get_transcript_html(self):
        """ Scrape site for transcript and returns all speech sections in a list """
        transcript_url = 'http://time.com/4912055/donald-trump-phoenix-arizona-transcript/'
        transcript_url_request = urlopen(transcript_url)
        transcript_html = transcript_url_request.read()
        transcript_html = transcript_html.decode('utf-8')
        transcript_list = bs.BeautifulSoup(transcript_html, "lxml").find_all('figure', attrs={"class":"blockquote"})
        dialouge_list = re.findall( '<p>TRUMP: (.*?)</p>', str(transcript_list), re.DOTALL)
        return dialouge_list

    def _write_to_text_file(self, dialouge_list):
        scraped_file = Path("transcript.txt")
        if scraped_file.is_file():
            f = open("transcript.txt","a+")
            for sentence in dialouge_list:
                f.write(sentence)
        else:
            f = open("transcript.txt","w+")
            for sentence in dialouge_list:
                f.write(sentence)

    def scrape(self):
        dialouge_list = self._get_transcript_html()
        self._write_to_text_file(dialouge_list)

Scrape()


    # def _remove_punctuation(self, long_string):
    #     """ Generates all dialouge of Trump in a single string """
    #     long_string = ' '.join(dialouge_list)
    #     long_string = ''.join(c for c in long_string if c not in punctuation)
    #     self._write_to_text_file(long_string)
    #
    # def _single_words(self, long_string):
    #     """ Given dailouge list, return a list seperated by words """
    #     with open('transcript.txt', 'r') as myfile:
    #         long_string = myfile.read()
    #     word_list = long_string.split()
    #     return word_list
    #
    # def scrape(self):
    #     """ Start scrape script and return list of single words """
    #     dialouge_list = self._get_transcript_html()
    #     long_string = self._remove_punctuation(dialouge_list)
    #     word_list = self._single_words(long_string)
    #     return word_list


# word_list = run_srape()
# fish_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
# x = Listogram(fish_text)
# print(len(x))
# x._index("blue")
# print_histogram(fish_text)


# def _get_words(source_text):
#     word_list = []
#     for sentence in source_text:
#         word_list.append(sentence.split(' '))
#     combined_word_list = [inner for outer in word_list for inner in outer]
#     remove_unicode = [word.strip('\xa0') for word in combined_word_list]
#     for word in remove_unicode:
#         if "</i>" in word:
#             remove_unicode.remove(word)
#     for word in remove_unicode:
#         if "<i>" in word:
#             remove_unicode.remove(word)
#     return remove_unicode
#
# only_words = _get_words(source_text)
#
# def histrogram(only_words):
#     word_count = {}
#     for word in only_words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count
#
# histo_dict = histrogram(only_words)
#
# def sort_histogram(histo_dict):
#     value_list = histo_dict.values()
#     list_values = list(value_list)
#     list_values.sort()
#     sorted_values = sorted(histo_dict, key=lambda x: histo_dict[x])
#     for k in sorted_values:
#         answer = "{} : {}".format(k, histo_dict[k])
#
#
#
# sort_histogram(histo_dict)
