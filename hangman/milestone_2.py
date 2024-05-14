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
guess : str


if __name__ == "__main__":
    #print word list
    print(word_list)
    #print random word
    # random.choice(word_list)
    print(word)

    guess = input('Please Enter a single Character\n')
    # print(guess)
    if len(guess) == 1:
        print('Good guess!')
    else:
        print('Oops! That is not a vlaid input')