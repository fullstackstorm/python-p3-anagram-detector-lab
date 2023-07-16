class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert word to lowercase for case-insensitive comparison

    def is_anagram(self, other_word):
        # Convert both words to lowercase and sort the characters
        return sorted(self.word) == sorted(other_word.lower())

    def match(self, anagram_list):
        # Filter the anagram_list to find all anagrams of the given word
        return [word for word in anagram_list if self.is_anagram(word)]
