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

def constraint(txt):
    if pangram(txt):
        return "Pangram"
    elif heterogram(txt):
        return "Heterogram"
    elif tautogram(txt):
        return "Tautogram"
    elif transgram(txt):
        return "Transgram"
    else:
        return "Sentence"
​
​
def get_chars(txt):
    lst = []
    for char in txt:
        if char.isalpha():
            lst.append(char.lower())
    return lst
​
​
def pangram(txt):
    correct = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lst = get_chars(txt)
​
    if sorted(set(lst)) == correct:
        return True
    return False
​
​
def heterogram(txt):
    lst = get_chars(txt)
​
    for char in lst:
        if lst.count(char) != 1:
            return False
    return True
​
​
def tautogram(txt):
    lst = txt.split(" ")
    first = lst[0][0].lower()
​
    for word in lst:
        if word[0].lower() != first:
            return False
    return True
​
​
def transgram(txt):
    lst = sorted(txt.split(" "), key=len)
    check = []
​
    for char in lst[0]:
        is_successful = True
​
        for i in range(len(lst)):
            if char.lower() not in lst[i].lower():
                check.append(0)
                is_successful = False
                break
        
        if is_successful:
            check.append(1)
    
    if 1 in check:
        return True
    return False

