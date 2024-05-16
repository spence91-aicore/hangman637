import random
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

    # word_list : List[str]
    num_list : int
    num_letters : int
    num_lives : int
    word : str 
    word_guessed : List[str]
    list_of_guesses : List[str] = []
    

    def __init__(self, word_list : List[str], num_lives : int = 5) -> None:

        #pick a word at random from the list
        self.word = random.choice(word_list)
        self.word_guessed : List[str] = list(['_' for i in self.word])
        self.num_lives = num_lives
        # getting unique letters
        unique_letters = set(self.word)
        self.num_letters = len(unique_letters)



    def check_guess(self, guess : str) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # update word_guessed, to reflect the correct guess
            for index in range(len(self.word)):
                if guess == self.word[index]:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1  
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
  
        return

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
    word_list = ['apple']
    game = Hangman(word_list, num_lives=5)
    # game.list_of_guesses = ['a','o']
    game.ask_for_input()
    print(game.list_of_guesses)
    print(game.word_guessed)
    print(game.num_letters)
    print(game.word_guessed)

    # play_game(word_list)