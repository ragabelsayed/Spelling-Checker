from spelling_checker import SpellingChecker

# Example usage:
dictionary_file = "dictionary.txt"
checker = SpellingChecker(dictionary_file)

input_word = "apple"
print(checker.check_spelling(input_word))

input_word = "banan"
print(checker.check_spelling(input_word))

new_word = "banana"
checker.add_word(new_word)
print(f"'{new_word}' has been added to the dictionary.")