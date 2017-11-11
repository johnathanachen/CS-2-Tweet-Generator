def remove_punctuation(dialouge_list):
    """ Given dialouge_list, remove all symbols such as period, question marks, period, etc """
    long_string = ' '.join(dialouge_list)
    long_string = ''.join(c for c in long_string if c not in punctuation)
    return long_string
