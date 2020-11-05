import random

HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
        |
    =========''','''

    +---+
    |   |
   [O]  |
        |
        |
        |
        |
    =========''','''
    +---+
    |   |
   [O]  |
    |   |
        |
        |
        |
    =========''','''
    +---+
    |   |
   [O]  |
   /|   |
        |
        |
        |
    =========''',r'''
    +---+
    |   |
   [O]  |
   /|\  |
        |
        |
        |
    =========''',r'''
    +---+
    |   |
   [O]  |
   /|\  |
   /    |
        |
        |
    =========''',r'''
    +---+
    |   |
   [O]  |
   /|\  |
   / \  |
        |
        |
    =========''']

#print(HANGMANPICS[-1])

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'''

words = words.split(" ")
print(words)

def RandomWord(wordlist):
    '''This function returns a random string from words list of string'''
    wordindex = random.randint(0, len(wordlist))
    return wordlist[wordindex]

def displayboard(HANGMANPICS,missedletters, correctletters, secretword):
    '''This function displays the board'''
    print(HANGMANPICS[len(missedletters)])
    print()
    print("Missed letters: ", end=' ')
    for letter in missedletters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretword)

    # replace the blank with correctword
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    
    print()

def getGuess(alreadyGussed):
    '''Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.'''
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please Enter a single letter")
        elif guess in alreadyGussed:
            print("You have already guessed that letter")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please Enter a letter")
        else:
            return guess

def playAgain():
    '''Returns True if player chooses yes else False'''
    choice = input("Do you want to play again? say [YES/NO]: ")
    if choice[0].lower().startswith('y'):
        return True
    return False

def main():
    missedletters = ''
    correctletters = ''
    secretword = RandomWord(wordlist=words)
    gameisdone = False
    foundAllLetters = False
    while True:
        displayboard(HANGMANPICS, missedletters, correctletters, secretword)

        # Let the player guess

        guess = getGuess(missedletters+correctletters)

        if guess in secretword:
            correctletters = correctletters + guess
            # check if player has won
            foundAllLetters = True
            for i in range(len(secretword)):
                if secretword[i] not in correctletters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                displayboard(HANGMANPICS,missedletters,correctletters,secretword)
                print("Yes the secret word is {}! You have won!!".format(secretword))
                gameisdone = True
        else:
            missedletters = missedletters + guess

            # check the player has guessed too many times
            if len(missedletters) == len(HANGMANPICS)-1:
                displayboard(HANGMANPICS, missedletters, correctletters, secretword)
                print("You have run out of guesses \nafter {a} missed guesses and {b} correct guesses".format(a=str(len(missedletters)),b=str(len(correctletters))))
                print("The secretword was: {}".format(secretword))
                gameisdone = True
                
            
        if gameisdone:
            if playAgain() == True:
                missedletters = ''
                correctletters = ''
                gameisdone = False
                secretword = RandomWord(words)
            else:
                print("Thanks for playing")
                break

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
