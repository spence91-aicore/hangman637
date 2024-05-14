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
guess : str = ""

def is_single_character(guess:str) -> bool:
    '''checks to see if string is a single character. Returns a True or a False'''
    if len(guess) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    #print word list
    print(word_list)
    #print random word
    # random.choice(word_list)
    print(word)

    guess = input('Please Enter a single Character\n')
    # print(guess)
    if is_single_character():
        print('Good guess!')
    else:
        print('Oops! That is not a vlaid input')