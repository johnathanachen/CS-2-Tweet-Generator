from histograms import Dictogram
import random
from collections import deque
import re


def markov_chain(data):
    """markov model for 1st order"""
    #Dictionary that stores windows as the key in the key-value pair and then the value
    #for each key is a dictogram
    markov_chain = dict()
    # Looping through the ammount of indexs in the list
    for index in range(0, len(data) - 1):
        # If index word of list exists in dictionary then update the current index
        # Store a histogram of words for each window
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    return markov_chain

# Walk our model
def generate_random_start(model):
    # Generate a "valid" starting word.
    # A valid starting word are words that start a sentence
    if 'END' in model:
        end_word = 'END'
        while end_word == 'END':
            end_word = model['END'].return_weighted_random_word()
        return end_word
    return random.choice(list(model.keys()))
    pass

# Generating sentence using first order markov_model
def generate_sentence(length, markov_model):
    # length parameter is length of the sentence
    # Create first word
    current_word = generate_random_start(markov_model)
    # Save first word to sentence list
    sentence = [current_word]
    # Loop through the length of sentence provided
    for i in range(0, length):
        # Getting current dictogram and starting from the current word(first word)
        current_dictogram = markov_model[current_word]
        # Getting random word from dictogram starting from the place of the current word
        random_word = current_dictogram.return_weighted_random_word()
        # Setting current word variable to the random word
        current_word = random_word
        # Append the new current word until the sentence length is formed
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence


if __name__ == '__main__':
    clean_text_list = ["how", "much", "wood", "would", "a", "wood", "chuck", "chuck", "if", "a", "wood", "chuck", "could", "chuck", "wood"]
    markov_chain = markov_chain(clean_text_list)
    generate_random_start(markov_chain)
    sentence = generate_sentence(10, markov_chain)
    # # sentence = generate_sentence_with_higher_order(10, higher_order_markov_chain)
    print(sentence)
