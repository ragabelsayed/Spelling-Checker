class SpellingChecker:
    def __init__(self, dictionary_file):
        """
        Store and load the dictionary.
        
        Args:
            dictionary file: file that have words to read from.
        """
        self.dictionary = set()
        self.load_dictionary(dictionary_file)

    # Load the dictionary from the txt file and store it in a set
    # Time Complexity: O(n), where n is the number of words in the dictionary file
    # Space Complexity: O(n), where n is the number of words in the dictionary file
    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r', encoding='cp437') as file:
            for word in file:
                self.dictionary.add(word.strip())
                
    # Check if the input word is in the dictionary.
    # If not, return the nearest 4 words in lexicographic order if they exist.
    # Time Complexity: O(n log n) in the worst case, where n is the number of words in the dictionary
    # Space Complexity: O(n), where n is the number of words in the dictionary 
    def check_spelling(self, word):
        if word in self.dictionary:
            return f"{word} is spelled correctly."

        nearest_words = []
        word_list = sorted(list(self.dictionary))
        
        for w in word_list:
            if w > word:
                nearest_words.append(w)
                if len(nearest_words) == 4:
                    break

        return f"{word} is not in the dictionary. Nearest words: {', '.join(nearest_words)}"
    
    # Add the input word to the dictionary.
    # Time Complexity: O(1) for adding a word to a set
    # Space Complexity: O(1)       
    def add_word(self, word):
        """
        Adds the given word to the dictionary.

        Args:
            word (str): The word to add to the dictionary.
        """
        self.dictionary.add(word)
        