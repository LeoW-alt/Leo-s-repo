Text Analyzer & Dictionary Tool (Python)

A Python command-line program that analyzes text and provides dictionary lookups.
It supports text statistics, palindrome detection, word frequency analysis, and dictionary definitions, synonyms, and antonyms with a fallback system.

***Features****

---Text Analysis----
.Character count (with and without spaces)
.Word count
.Sentence count
.Most common word (excluding common stop words)
.Palindrome word detection
.Count how many times a specific word appears

---Input Options----
.Enter text manually
.Read text from a file (via file path)

---Dictionary Lookup----
.Definitions
.Synonyms
.Antonyms
.Uses PyDictionary
.Falls back to WordNet (NLTK) if PyDictionary fail

****Requirements*****

Make sure you have Python 3.8+ installed.

Install required libraries(run in terminal):
pip install PyDictionary nltk

Download WordNet data (run once):
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

How to Run
python sentence_and_word.py


You’ll see a menu like:

--- TEXT ANALYZER MENU ---
1. Enter text manually
2. Read text from file
3. Dictionary Lookup
4. Exit

📂 File Input Example

When choosing file input, enter either:
A file name in the same directory
sample.txt

Or a full file path

C:\Users\YourName\Documents\text.txt

🧠 How It Works (Quick Overview)
Text is cleaned (lowercased, punctuation removed)
Words are analyzed using Python data structures
Palindromes are detected using string slicing

Dictionary lookups:
First try PyDictionary
If it fails, use WordNet (NLTK) as a fallback

Known Limitations
Dictionary results depend on API availability
Some words may not return synonyms/antonyms
Sentence detection is basic (punctuation-based)

Learning Goals

This project demonstrates:
Functions and modular programming
Dictionaries and sets
File handling
Error handling (try / except)
External libraries and API fallbacks
Menu-driven CLI programs

Contribution

This is a learning project.
Feel free to fork, modify, or improve it.

License

MIT License — free to use, modify, and distribute.