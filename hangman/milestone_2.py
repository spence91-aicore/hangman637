import random
import typing
from typing import List


word_list : List[str] = \
    ['pineapple',
     'apple',
     'blueberry',
     'raspberry',
     'kiwi'
    ]

word = random.choice(word_list)

if __name__ == "__main__":
    #print word list
    print(word_list)
    #print random word
    # random.choice(word_list)
    print(word)