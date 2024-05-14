from milestone_2 import is_single_character, word, guess


def is_alpha_character(word:str) -> bool:
    '''checks to see if the string is an alphabetical character'''
    if is_single_character(word) == False:
        raise ValueError('single character required')
 
    return word.isalpha()


def is_guess_in_word(guess:str, word:str) -> bool:
    '''returns True if '''
    if guess in word:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:      
        guess = input('Please Enter a single Character\n')
        if is_single_character(guess) == False or is_alpha_character(guess) == False:
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue
        if is_guess_in_word(guess,word):
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

