# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/22
# Gets the user input for a sentence. Uses a function
# To turn that sentence into a list of strings which are then
# Separates and displayed back to the user.


# Function to parse the string
def string_parser(sentence_list):
    words = sentence_list
    # Split the sentence into a list
    sentence = words.split(" ")
    # Join the list back into words separated by a newline and return it
    return "\n".join(sentence)


def main():
    # Title of the program
    print("String Parser")

    # user input for the sentence
    user_sentence_string = input("Please enter a sentence: ")

    # TRY CATCH to check if the input is a string
    try:
        user_sentence = str(user_sentence_string)

    except Exception:
        print("Please enter a string!")

    else:
        # Call the function and display the words
        sentence = string_parser(user_sentence)
        print("The words in your sentence are:")
        print(sentence)


if __name__ == "__main__":
    main()
