"""


Write a function that takes a string, breaks it up and returns it with vowels
first, consonants second. For any character that's not a vowel (like special
characters or spaces), treat them like consonants.

### Examples

    split("abcde") ➞ "aebcd"
    
    split("Hello!") ➞ "eoHll!"
    
    split("What's the time?") ➞ "aeieWht's th tm?"

### Notes

  * Vowels are `a, e, i, o, u`.
  * Define a separate `is_vowel()` function for easier to read code (recommendation).

"""

def split(txt):
    new_sentence = ""
    for char in txt:
        if is_vowel(char):
            new_sentence += char
​
    for char in txt:
        if not is_vowel(char):
            new_sentence += char
​
    return new_sentence
​
​
def is_vowel(character):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if character in vowels:
        return True
    return False

