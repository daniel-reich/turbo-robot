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

def Pangram(txt):
    a = "abcdefghijklmnopqrstuvwxyz"
    s = [x for x in set(txt.lower())]
    t = 0
    for i in s:
        if i in a:
            t +=1
    if t==26:
     return True
def Heterogram(txt):
    s = [x for x in set(txt.lower()) if x.isalpha()]
    s2 = [x for x in txt.lower() if x.isalpha()]
    if len(s) == len(s2):
     return True
def Tautogram(txt):
    t = txt.lower().split()
    s = t[0][0].lower()
    for i in range(len(t)):
        if t[i][0] != s:
            return False
    return True
def Transgram(txt):
    t = txt.lower().split()
    s = t[0]
    for i in s:
        l = []
        for j in t:
            if i in j:
                l.append(i)
        if len(l) == len(t):
          return True
​
def constraint(txt):
    if Pangram(txt):
        return "Pangram"
    elif Heterogram(txt):
        return "Heterogram"
    elif Tautogram(txt):
        return "Tautogram"
    elif Transgram(txt):
        return "Transgram"
    else:
        return "Sentence"

