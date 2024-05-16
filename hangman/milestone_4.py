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
    list_of_guesses : List[str] = []
    

    def __init__(self, word_list : List[str], num_lives : int = 5) -> None:
        pass

    def check_guess(self, guess : str) -> None:
        pass

    @staticmethod
    def _is_alpha_character(guess:str) -> bool:
        '''checks to see if the string is an alphabetical character'''
        return guess.isalpha()

    @staticmethod
    def _is_single_character(guess:str) -> bool:
        '''checks to see if string is a single character. Returns a True or a False'''
        return len(guess) == 1

    def _is_already_guessed(self,guess:str) -> bool:
        '''checks the guess against previous guesses'''
        return guess in self.list_of_guesses


    def ask_for_input(self) -> None:
        '''reads input for a guess, and will return the guess variable'''
        guess = ""
        while True:      
            guess = input('Please Enter a single Character\n')
            guess = guess.lower()
            # check to see if input is valid, continue until we get a valid char
            if self._is_single_character(guess) == False or self._is_alpha_character(guess) == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
                continue
            # check if it's already been guessed, continue until we get an un-guessed char
            elif self._is_already_guessed(guess):
                print('You already tried that letter!')
                continue
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            break
        return guess
    
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    game = Hangman(word_list, num_lives=5)
    game.list_of_guesses = ['a','o']
    game.ask_for_input()
    print(game.list_of_guesses)

    # play_game(word_list)