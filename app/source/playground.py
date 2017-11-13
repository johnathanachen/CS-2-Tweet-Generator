word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
word_count = []

for word in word_list:
    if word in word_count:
        # word_count[word_element][1] += 1
        print("got it")
        print(self.word_count[word_element][1])
    else:
        word_element = [word]
        word_count.append(word_element)
        word_element.append(1)

print(word_count)
