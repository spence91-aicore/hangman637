from milestone_2 import is_single_character, word, guess



def is_alpha_character(guess:str) -> bool:
    '''checks to see if the string is an alphabetical character'''
    if is_single_character(guess) == False:
        raise ValueError('single character required')
 
    return guess.isalpha()


def is_guess_in_word(guess:str) -> bool:
    '''returns True if the guess character is in word string '''
    if guess in word:
        return True
    else:
        return False
    
def check_guess(guess : str, word : str) -> None:
    ''''''
    guess = guess.lower()
    if is_guess_in_word(guess):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")    
    return

def ask_for_input() -> str:
    '''reads input for a guess, and will return the guess variable'''
    guess = ""
    while True:      
        guess = input('Please Enter a single Character\n')
        if is_single_character(guess) == False or is_alpha_character(guess) == False:
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue
        break
    return guess

if __name__ == "__main__":
        guess = ask_for_input()
        check_guess(guess, word)


