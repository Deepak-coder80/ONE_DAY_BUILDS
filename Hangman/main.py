import random

#create sample wordlist
word_list = ["aardvark", "baboon", "camel"]

#choose a word from the wordlist
chosen_word = random.choice(word_list)

#read a character from the user
guess = input("Enter a character : ").lower()

#look for the matched letter
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
            print("Wrong")
