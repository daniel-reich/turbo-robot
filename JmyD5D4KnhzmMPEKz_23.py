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

import string
def constraint(txt):
    x = string.ascii_lowercase
    txt = txt.lower()
    if is_pangram(txt, x):      return 'Pangram'
    if is_heterogram(txt):      return 'Heterogram'
    if is_tautogram(txt):       return 'Tautogram'
    if is_transgram(txt):       return 'Transgram'
    return 'Sentence'
​
def is_pangram(txt, x):
    for ch in x:
        if ch not in txt:
            return False
    return True
​
def is_heterogram(txt):
    for ch in txt:
        if ch.isalpha() and txt.count(ch) != 1:
            return False
    return True
​
def is_tautogram(txt):
    return len(set([x[0] for x in txt.split()])) == 1
​
def is_transgram(txt):
    los = [set(x) for x in txt.split()]
    return len(set.intersection(*los)) > 0

