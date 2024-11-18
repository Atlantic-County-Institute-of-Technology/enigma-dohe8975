# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Gates Doherty
# created: 11/18/2024
# last update:  11/18/2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message(UserIn, UserKey):
    out_string = ""
    for i in range(len(UserIn)):
        x = ord(UserIn[i]) + UserKey
        print(x)
        if 65 <= x <= 90:
            out_string += chr(x)
        if 97 <= x <= 122:
            out_string += chr(x)
        if x + UserKey >= 123:
            x = ord(UserIn[i]) + UserKey - 26
            out_string += chr(x)
    print(out_string)

    out_string = ""
    for char in UserIn:
        if 65 <= ord(char) <= 90:
         # uppercase to lower case
         out_string += chr(ord(char) + 32)
         # lowercase to uppercase
        elif 97 <= ord(char) <= 122:
            out_string += chr(ord(char) - 32)
        else:
            out_string += char



# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            UserIn = str(input("Please enter the message you'd like to encode: "))
            UserKey = int(input("Enter the rotational cipher key. (Press enter for a random value): "))
            encode_message(UserIn, UserKey)

        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()