
# alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# read inputs
# 1.read whether user want to encode or decode
direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt message : \n")
# read the input  text
text = input("Type your message : ").lower()
# read number of shift want
shift = int(input('Type the shift number : '))

# encrypt function
def encrypt(text, shifts):
    # return text
    cipher_text = ""
    # shift each character in the text shiftted up
    # with number of shifts
    for letter in text:
        #if letter is space or fullstop
        if(letter==' 'or letter =='.'):
            #add it directly
            cipher_text+=letter
            continue
        # find index of letter from alphbet list
        current_index = alphabet.index(letter)
        # find the new_index:
        new_index = current_index+shifts
        # find letter in the new_index
        new_letter = alphabet[new_index]
        # append new_letter to cipher text:
        cipher_text += new_letter
    # print the encrypted text
    print(f"The encoded text is {cipher_text}")

# encrypt function
def decrypt(text, shifts):
    # return text
    caesar_text = ""
    # shift each character in the text shiftted up
    # with number of shifts
    for letter in text:
         #if letter is space or fullstop
        if(letter==' 'or letter =='.'):
            #add it directly
            caesar_text+=letter
            continue
        # find index of letter from alphbet list
        current_index = alphabet.index(letter)
        # find the new_index:
        new_index = current_index-shifts
        # find letter in the new_index
        new_letter = alphabet[new_index]
        # append new_letter to cipher text:
        caesar_text += new_letter
    # print the encrypted text
    print(f"The decoded text is {caesar_text}")

# call the function corresponding to direction variable
if(direction=='encode'):
    encrypt(text, shift)
elif(direction=='decode'):
    decrypt(text, shift)
else:
    print("Please check your inputs")