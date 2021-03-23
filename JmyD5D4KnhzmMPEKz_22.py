"""


In this challenge, establish which type of constrained writing is applied to a
sentence. There are four possible types to detect:

  *  **Pangram** : the sentence contains all the 26 letters of the English alphabet.
  *  **Heterogram** : the sentence doesn't have multiple instances of its letters (as to say that every letter is unique).
  *  **Tautogram** : every word of the sentence starts with the same letter.
  *  **Transgram** : all words of the sentence share at least a common letter.

Given a string `txt` being a sentence, implement a function that returns the
strings `"Pangram"`, `"Heterogram"`, `"Tautogram"` or `"Transgram"`
accordingly to the above definitions and following the same given order to
establish the result. If no constrained writing is detected, return the string
`"Sentence"`.

### Examples

    constraint("The quick brown fox jumps over the lazy dog.") ➞ "Pangram"
    # The sentence contains every letter of the alphabet.
    # Repetitions are not considered.
    
    constraint("The big dwarf only jumps.") ➞ "Heterogram"
    # The sentence has only unique characters.
    
    constraint("Todd told Tom to take the tiny turtles.") ➞ "Tautogram"
    # Every word starts with the letter "t".
    
    constraint("A cannibal alligator has attacked an unaware vegan alligator.") ➞ "Transgram"
    # Every word contains the letter "a".
    
    constraint("The unbearable lightness of coding...") ➞ "Sentence"
    # No constraint is applied to the sentence.

### Notes

  * Remember to respect the given order to establish the result: a **Pangram** has to be detected before a **Heterogram** , and a **Tautogram** has to be detected before a **Transgram**.
  * Sentences will contain letters (either uppercase or lowercase) and punctuation. Your function must be case-insensitive.

"""

from string import ascii_lowercase
from collections import Counter
​
def constraint(txt):
    txt = txt.lower()
​
    def pangram(txt):
        result = set(
            i for i in txt if i.isalpha()
        ) == set(ascii_lowercase)
        return 'Pangram' if result else (heterogram(txt))
​
    def heterogram(txt):
        c = Counter(i for i in txt if i.isalpha())
        d = Counter(ascii_lowercase)
        result = not c - d
        return 'Heterogram' if result else (tautogram(txt))
​
    def tautogram(txt):
        result = len(set(i[0] for i in txt.split())) == 1
        return 'Tautogram' if result else (transgram(txt))
​
    def transgram(txt):
        first, *rest = (
            tuple(i) for i in txt.split() if i.isalpha())
        result = set(first).intersection(*rest)
        return 'Transgram' if result else 'Sentence'
​
    return pangram(txt)

