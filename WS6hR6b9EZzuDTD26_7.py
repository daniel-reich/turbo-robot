"""


Given a common phrase, return `False` if _any_ individual word in the phrase
contains _duplicate_ letters. Return `True` otherwise.

### Examples

    no_duplicate_letters("Fortune favours the bold.") ➞ True
    
    no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
    
    no_duplicate_letters("Look before you leap.") ➞ False
    # Duplicate letters in "Look" and "before".
    
    no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".

### Notes

Letter matches are case-insensitive.

"""

def no_duplicate_letters(phrase):
  noDups = True
  words = phrase.split(" ")
  print(words)
  for word in words:
    if not noDups:
      break
    previouslyUsed = []
    for letter in word:
      if letter in previouslyUsed:
        noDups = False
        break
      previouslyUsed.append(letter)
  return noDups

