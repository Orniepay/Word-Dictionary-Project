from PyDictionary import PyDictionary

print()
print("Word Dictionary: ")
print("=================")

dictionary = PyDictionary

def get_word_meaning(word):
    """
    Retrieves the meaning of a given word.

    This function uses the PyDictionary module to look up the meaning of the input word.
    It fetches and prints the definition(s) of the word from various parts of speech.
    If the word does not exist or an error occurs, it prints a message indicating the 
    absence of a definition.

    Parameters:
    word (str): The word for which the meaning is to be found.

    Returns:
    None: The function prints the meaning(s) of the word and does not return a value.
    """
    return dictionary.meaning(word)

while True:
    print()
    word = input("Enter your word: ")
    if word == "":
        print()
        break
    print()
    print(dictionary.meaning(word))