##TEXT ANALYZER AND DICTIONARY

import string
from PyDictionary import PyDictionary
from nltk.corpus import wordnet

# Initialize dictionary
py_dictionary = PyDictionary()

#Common words to exclude
common = {
    "the", "and", "is", "in", "to", "of", "a", "an", "on", "for", "with",
    "as", "by", "at", "from", "it", "this", "that", "be", "are", "was", "i"
}

#         TEXT CLEANING
def clean_text(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char,"")
    return text

#         PALINDROME CHECK    
def is_palindrome(word):
    return word == word[::-1] and len(word) > 1

#         TEXT ANALYSIS
def analyze_text(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    sentences = [s for s in text.replace("!",".").replace("?",".").split(".") if s.strip()]

    char_count = len(text)
    char_no_spaces = len(text.replace(" ", ""))
    word_count = len(words)
    sentence_count = len(sentences)

    word_frequency = {}
    palindromes = set()

    for word  in words:
        if word not in common:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        if is_palindrome(word):
            palindromes.add(word)

    print("\n--- TEXT ANALYSIS RESULTS ---")
    print(f"Total characters (with spaces): {char_count}")
    print(f"Total characters (no spaces): {char_no_spaces}")
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")

    if word_frequency:
        most_common = max(word_frequency, key=word_frequency.get)
        print(f"Most used word (excluding common words): '{most_common}'")

    print("\n Palindrome words found:")
    if palindromes:
        print(", ".join(palindromes))    
    else:
        print("None found.")

    return words

#          WORD SEARCH
def count_specific_word(words):
    word = clean_text(input("Enter the word to search for: "))
    print(f"'{word}' appears {words.count(word)} time(s).") 

#           FILE INPUT
def read_from_file():
    filename = input("Enter file name or path: ")
    try:
        with open(filename, "r", encoding='utf-8',) as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")   
    return None

#          DICTIONARY
def dictionary_lookup():
    word = input("\nEnter word to look up: ").lower()

#First check in pydictionary
    meanings = py_dictionary.meaning(word)
    synonyms = py_dictionary.synonym(word)
    antonyms = py_dictionary.antonym(word)

    if meanings or synonyms or antonyms:
       print("\n--- RESULTS FROM PyDictionary ---")

       if meanings:
        print("\nMeanings:")
        for part, defs in meanings.items():
            print(f"{part}:")
            for d in defs:
                print(f" - {d}")
       else:
        print("No meanings found")

       if synonyms:
        print("\nSynonyms:")
        print(", ".join(synonyms))
       else:
        print("\nNo synonyms found.")

       if antonyms:
        print("\nAntonyms:")
        print(", ".join(antonyms))
       else:
        print("\nNo antonyms found.")  

       return
    
    #Falling back to wordnet if pydictionary doesn't have the word
    print("\nPyDictionary failed. Falling back to WordNet...")

    synsets = wordnet.synsets(word)

    if not synsets:
       print("No meanings found in WordNet either")
       return
    
    print("\n--- RESULTS FROM WORDNET ---")

    print("\nMeanings:")
    for syn in synsets[:3]:
       print(f" - {syn.definition()}")

    synonyms_set = set()
    antonyms_set = set()

    for syn in synsets:
       for lemma in syn.lemmas():
          synonyms_set.add(lemma.name())
          if lemma.antonyms():
             antonyms_set.add(lemma.antonyms()[0].name())

    if synonyms_set:
       print("\nSynonyms:")
       print(", ".join(sorted(synonyms_set)))
    else:
       print("No synonyms found.")

    if antonyms_set:
       print("\nAntonyms:")
       print(", ".join(sorted(antonyms_set)))
    else:
       print("No antonyms found.")                     

def menu():
    while True:
        print("\n--- TEXT ANALYZER MENU ---")
        print("1. Enter text manually") 
        print("2. Read text from file")
        print("3. Dictionary Lookup")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("\nEnter text:\n")
            words = analyze_text(text)
            count_specific_word(words)
        elif choice == "2":
            text = read_from_file()
            if text:
                words = analyze_text(text)
                count_specific_word(words)
        elif choice == "3":
            dictionary_lookup()    
        elif choice == "4":
            print("Thank You Bye")
            break
        else:
            print("Invalid choice. Try again.")

        
#PROGRAM START
menu()                               
