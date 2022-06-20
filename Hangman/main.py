import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

guess = input("Enter a character : ").lower()

for letter in chosen_word:
        if guess == letter:
                    print("Right")
                        else:
                                    print("Wrong")
