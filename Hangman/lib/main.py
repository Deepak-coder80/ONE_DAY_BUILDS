#genral imports
import random

#import word_list
from hangman_words import word_list 
#import HangMan Stages
import hangman_art

#life of user
lives = 7

#choose a word from the wordlist
chosen_word = random.choice(word_list)


#create a empty list for displaying word with '_' 
display =[]
#assign _ to list 
for letter in range(len(chosen_word)):
    display += "_"

#run guessing upto all the blanks filled
end_of_game = False

#print the logo
print(hangman_art.logo)
#intro text
print("\nWelcome To the game😍.Let's get into HangMans World🙌")
#rule
print(f"RULES:\n\t1.You have {lives} lives❤️.if you gives a wrong guess one life is gone 😣")
#hint Time
display[2]=chosen_word[2]
print(f"HINTS:\n\t1.The word have length {len(chosen_word)}.\n\tThe word : {display}")
#while loop
while not end_of_game:
    #status
    count=display.count('_')
    print(f"\nGame Status : \n\n No. of Life left ❤️ : {lives}\n Characters Left in the word : {count}")
    #read a character from the user
    guess = input("\nGuess a letter : ").lower()

    #if letter is already guessed
    if guess in display:
        print(f"\nYou've already guessed {guess}")
        continue

    #look for the matched letter and update display and print
    for position in range(len(chosen_word)):
        #get the letter
        letter = chosen_word[position]
        #check for equality
        if letter==guess:
            #update display list
            display[position]= letter 
            #correct guess 
            print("\nIt's a Correct Guess🎉🎉.Keep Going")        
    #if guessed letter not letter  
    if guess not in chosen_word:
        #let them know
        print(f"\nYou guessed {guess}, that's not in the word!you lose a life 😣")
        #reduce lives by one 
        lives -=1
        #check for lives
        if lives == 0:
            end_of_game=True;
            print("\nGame Over🤐.You Lost it 😔.Better Luck Next Time😊")
            print("\nMAN HANGED😶")
            print(hangman_art.stages[lives])
            continue
        #print hangMan stages corresponding to lives
        print(hangman_art.stages[lives])
    
    #print display
    print(f"\nThe Word : {''.join(display)}")

    #check there if there is any "_" left
    if "_" not in display:
        end_of_game=True
        print("WOW! YOU WON 🎉🎉🎉🎉 ")
    
    