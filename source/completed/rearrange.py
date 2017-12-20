import sys
import string
import random

def rearrange(*word_dump):
    word_list = list(word_dump)
    randomize = ' '.join(random.choice(word_list) for i in word_list)
    print(randomize)
    return randomize

if __name__ == "__main__":
    word_dump = sys.argv[1:]
    rearrange(*word_dump)
