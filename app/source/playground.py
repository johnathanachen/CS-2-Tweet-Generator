# word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
# word_count = []
#
# for word in word_list:
#     if word in word_count:
#         # word_count[word_element][1] += 1
#         print("got it")
#         print(self.word_count[word_element][1])
#     else:
#         word_element = [word]
#         word_count.append(word_element)
#         word_element.append(1)
#
# print(word_count)

only_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
word_count = []
added_words = []

for word in only_words:
    if word in added_words:
        count_up = word_count[arr_word[1]][1]
        count_up += 1
        print(count_up)
    else:
        arr_word = [word]
        word_count.append(arr_word)
        added_words.append(word)
        arr_word.append(1)
print(word_count)
