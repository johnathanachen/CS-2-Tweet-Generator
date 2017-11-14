from dictogram import Dictogram

li = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
histogram = Dictogram(li)
dictogram = histogram.word_count



def fish(li):
    histogram_fish_list = []
    counted_for = []
    token = 0
    running = True
    while running:
        for index, element in enumerate(li):
            this_element = element
            next_element = li[(index + 1) % len(li)]
        if this_element == "fish" and next_element not in counted_for:
            new_type = [next_element, 1]
            histogram_fish_list.append(new_type)
            counted_for.append(new_type)
        elif this_element == "fish" and next_element in counted_for:
            new_type[1] += 1
    print(histogram_fish_list)


def markov():
    """ Given a word, return five words """
    li = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    fish(li)


markov()
