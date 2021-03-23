"""


Create a function that takes a string and replaces each letter with its
appropriate position in the alphabet. "a" is 1, "b" is 2, "c" is 3, etc, etc.

### Examples

    alphabet_index("Wow, does that work?")
    ➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"
    
    alphabet_index("The river stole the gods.")
    ➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"
    
    alphabet_index("We have a lot of rain in June.")
    ➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"

### Notes

If any character in the string isn't a letter, ignore it.

"""

def alphabet_index(txt):
  result=''
  for character in txt:
    if character.isalpha():
      if character.isupper():
        result+=str(ord(character)-64)+' '
      else:
        result+=str(ord(character)-96)+' '
  return result[:-1]

