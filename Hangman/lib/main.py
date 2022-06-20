import random
#import word_list
from hangman_words import word_list 
#import HangMan Stages
import hangman_art

#life of user
lives =6

#create sample wordlist
word_list = ["aardvark", "baboon", "camel"]

#choose a word from the wordlist
chosen_word = random.choice(word_list)

#Test code --> REMOVE THIS
print(f'Selected Word : {chosen_word}')

#create a empty list for displaying word with '_' 
display =[]
#assign _ to list 
for letter in range(len(chosen_word)):
    display += "_"

#run guessing upto all the blanks filled
end_of_game = False

#print the logo
print(hangman_art.logo)
#while loop
while not end_of_game:
    #read a character from the user
    guess = input("Guess a letter : ").lower()

    #if letter is already guessed
    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    #look for the matched letter and update display and print
    for position in range(len(chosen_word)):
        #get the letter
        letter = chosen_word[position]
        #check for equality
        if letter==guess:
            #update display list
            display[position]= letter         
    #if guessed letter not letter  
    if guess not in chosen_word:
        #let them know
        print(f"You guessed {guess}, that's not in the word!you lose a life 😣")
        #reduce lives by one 
        lives -=1
        #check for lives
        if lives == 0:
            end_of_game=True;
            print("YOU LOST THE GAME!! BETTER LUCK NEXT TIME")
        #print hangMan stages corresponding to lives
        print(hangman_art.stages[lives])
        continue

    #print display
    print(f"{''.join(display)}")

    #check there if there is any "_" left
    if "_" not in display:
        end_of_game=True
        print("WOW! YOU WON ")
    
    