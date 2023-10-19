import random
def load_word():
    '''
    A function that reads an array of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    words_list = ["monkey", "autumn", "tree", "coffee", "patience", "sparrow", "homework", "computer" ]

    #words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

''' won_game = False

    available_guesses = 7
    letters_guessed = []
    #store guesses
    guess = input("Guess a letter: ")
    #store user input in guess var
    while won_game:
        #check if guess is == to a char in secret word
        if guess == chr in secret_word:
            ##append guess to list
            letters_guessed.append(guess)
            #if yes, print("__*_**"), and store
            print("Your guess appears in the secret word!" /n)
            print("Guessed word so far: ")
        #if no, print("try again!") and return remaining_guesses
        else:
            remaining_guesses -= available_guesses
            print("Your guess does not appear in the secret word!")
            print(f"remaining_guesses")
        ####remaining_guesses -= guesses
        #if char in guessed words == char in secret word, print secret word, return true
        ##if guessed letters == to letters in the secret word:
        when letters_guessed == secret_word:
        return True
        '''


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else: 
            guess += '_'
    return guessed_word
for i in data["cards"]: ##initiate the for loop for element 'i' in the list with key 'cards' in the 'data' dictionary.
    guess = input(i["q"] + " > ") //'i["q"]' retrieves value ass. with "q"



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    guess = input("Guess a letter:")
    
    if guess in secret_word:
        print(f"Your guess appears in the secret word!"'{guessed_word}')
    else:
        print(f"Your guess was not in the word. You have x remaining guesses.")
        #print remaining guesses





def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)