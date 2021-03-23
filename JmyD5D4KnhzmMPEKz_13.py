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
  def is_panagram(words):
    l8rs = ''
    a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    
    for word in words:
      l8rs += word
    
    for l8r in a:
      if l8r not in l8rs:
        return False
    return True
  def is_heterogram(words):
    l8rs = ''
    
    for word in words:
      l8rs += word
    
    s = set(l8rs)
    
    return len(l8rs) == len(list(s))
  def is_tautogram(words):
    
    imp_l8rs = []
    
    for word in words:
      imp_l8rs.append(word[0])
    
    s = list(set(imp_l8rs))
    
    return len(s) == 1
  def is_transgram(words):
    
    sets = []
    
    for word in words:
      sets.append(list(set(word)))
    
    for st in sets:
      for l8r in st:
        c = 0
        for s in sets:
          if l8r in s:
            c += 1
        if c == len(sets):
          return True
    return False
  
  words = txt.lower().split()
  
  panagram = is_panagram(words)
  heterogram = is_heterogram(words)
  tautogram = is_tautogram(words)
  transgram = is_transgram(words)
  
  if panagram == True:
    return 'Pangram'
  elif heterogram == True:
    return 'Heterogram'
  elif tautogram == True:
    return 'Tautogram'
  elif transgram == True:
    return 'Transgram'
  else:
    return 'Sentence'

