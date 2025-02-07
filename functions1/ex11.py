"""Write a Python function that checks whether a word or phrase is or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward
as forward, e.g., madampalindrome"""
def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word or phrase: ").replace(" ", "")

print(f"The word or phrase '{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")
# qazaq >>> The word or phrase 'qazaq' is a palindrome.
