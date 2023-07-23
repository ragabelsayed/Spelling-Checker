# Spelling-Checker

This is a Python implementation of a Spelling Checker, designed to help users check the spelling of words against a given dictionary. The main features of this Spelling Checker class are:

1. **Store Dictionary:** The class can load a dictionary from a txt file and store it in a suitable data structure. In this implementation, a set data structure is used for efficient word lookup.

2. **Check Spelling:** The Spelling Checker can take an input word and determine whether it exists in the loaded dictionary. If the word is not found in the dictionary, it provides the nearest four words (two words before and after) in lexicographic order, if they exist.

3. **Add Word:** Users can add new words to the dictionary using the `add_word` method. The new word will be appended to the existing dictionary for future spell checks.

**Functionality Overview:**

The main class, `SpellingChecker`, is designed with three essential methods:
1. `__init__(self, dictionary_file)`: The constructor of the class. It initializes the dictionary by loading words from the specified txt file.

2. `check_spelling(self, word)`: This method takes an input word and checks if it exists in the dictionary. If the word is present, it indicates that it is spelled correctly. Otherwise, it finds the nearest four words in lexicographic order and returns them as suggestions.

3. `add_word(self, word)`: This method allows the user to add a new word to the dictionary. The new word will be stored and used for future spell checks.

**How it Works:**

1. Upon instantiation, the class loads the dictionary from the provided txt file into a set data structure for quick lookups.

2. When the `check_spelling` method is called, it first checks if the input word exists in the dictionary. If found, it returns a message indicating that the word is spelled correctly.

3. If the input word is not present in the dictionary, the method searches for the nearest words in lexicographic order. It does so by sorting the dictionary and finding words greater than the input word. It appends up to four such words as suggestions.

4. The `add_word` method allows users to add new words to the dictionary by simply adding them to the set.

**Time and Space Complexity:**

- The `load_dictionary` method has a time complexity of O(n) and a space complexity of O(n), where n is the number of words in the dictionary file.

- The `check_spelling` method has a time complexity of O(n log n) and a space complexity of O(n), where n is the number of words in the dictionary.

- The `add_word` method has a time complexity of O(1) and a space complexity of O(1).

**Note:**

The provided Python implementation aims to offer a simple and efficient solution to the Spelling Checker task. It uses a sorted list of words to find the nearest suggestions for an input word. the current approach provides a more straightforward and easier-to-understand solution.

