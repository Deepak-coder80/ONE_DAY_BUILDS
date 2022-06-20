import random

#HangMan Stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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

#while loop
while not end_of_game:
    #read a character from the user
    guess = input("Enter a character : ").lower()

    #look for the matched letter and update display and print
    for position in range(len(chosen_word)):
        #get the letter
        letter = chosen_word[position]
        #check for equality
        if letter==guess:
            #update display list
            display[position]= letter    

    #print display
    print(display)

    #check there if there is any "_" left
    if "_" not in display:
        end_of_game=True