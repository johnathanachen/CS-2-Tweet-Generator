from string import punctuation

class Clean():

    def __init__(self, file_name):
        self.file_name = file_name
        self = self.clean_text(self.file_name)

    def _remove_punctuation(self, file_name):
        """ """
        with open(file_name, 'r') as myfile:
            dialouge_list = myfile.read()
        long_string = ''.join(dialouge_list)
        long_string = ''.join(c for c in long_string if c not in punctuation)
        print(long_string)
    # def _single_words(self, long_string):
    #     """ Given dailouge list, return a list seperated by words """
    #     with open('transcript.txt', 'r') as myfile:
    #         long_string = myfile.read()
    #     word_list = long_string.split()
    #     return word_list

    def clean_text(self, file_name):
        long_string = self._remove_punctuation(file_name)
        # word_list = self._single_words(long_string)
        # return word_list

file_name = "transcript.txt"
Clean(file_name)
