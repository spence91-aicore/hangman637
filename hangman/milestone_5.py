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
    num_letters: int
        number of uniq letters in word that needs to be guessed
    num_lives: int
        number of lives the player has left
    word: str
        the word that needs to be guessed, chosed at random from the list provided (word_list)
    word_guessed: List[str]
        a visual of the players progress, starts with all chars as '_', which will be revelaved as the player guesses correctly 
    list_of_guesses : List[str]
        a list of characters the player has already guessed, which will be added to with each guess
    '''

    num_letters : int
    num_lives : int
    word : str 
    word_guessed : List[str]
    list_of_guesses : List[str] = []
    

    def __init__(self, word_list : List[str], num_lives : int = 5) -> None:
        self.num_lives = num_lives
        #pick a word at random from the list
        self.word = random.choice(word_list)
        # init the word_guessed list - fill with '_' chars
        self.word_guessed : List[str] = list(['_' for i in self.word])
        # getting unique letters
        unique_letters = set(self.word)
        self.num_letters = len(unique_letters)


    def check_guess(self, guess : str) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # update word_guessed, to reflect the correct guess
            for index in range(len(self.word)):
                if guess == self.word[index]:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            #reduce num lives for bad guess
            self.num_lives -= 1  
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
  
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

def play_game(word_list):
    # As an aid, part of the code is already provided:
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(game.word_guessed)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        if game.num_letters > 0:
            game.ask_for_input()
            print(game.word_guessed)
        if game.num_lives != 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
