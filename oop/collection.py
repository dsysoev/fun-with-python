import string
import random

from collections import defaultdict
from collections import Counter

def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

if __name__ in '__main__':
    random.seed(37)
    sentence = ''
    for _ in range(10):
        sentence += random.choice(string.ascii_letters)

    freq = letter_frequency(sentence)
    print('sentence   : {}'.format(sentence))
    print('defaultdict: {}'.format(freq))
    print('Counter    : {}'.format(Counter(sentence)))
