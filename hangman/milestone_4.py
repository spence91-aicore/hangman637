from typing import List

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    '''

    word_list : List[str]
    num_list : int
    num_letters : int
    word : str 
    word_guessed : List[str]
    list_of_guesses : List[str]
    

    def __init__(self, word_list : List[str], num_lives : int = 5) -> None:
        pass