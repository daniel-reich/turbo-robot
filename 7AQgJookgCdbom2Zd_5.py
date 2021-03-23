"""


Create a function that takes a string of words and moves the first letter of
each word to the end of it, then adds 'ay' to the end of the word. This is
called "Pig Latin" and it gets more complicated than the rules in this
particular challenge. I've intentionally kept things simple, otherwise this
would turn into an extremely tedious challenge.

  * Move the first letter of each word to the end of the word.
  * Add "ay" to the end of the word.
  * Words starting with a vowel (A, E, I, O, U) simply have "WAY" appended to the end.

### Examples

    pig_latin("Cats are great pets.")
    ➞ "Atscay areway reatgay etspay."
    
    pig_latin("Tom got a small piece of pie.")
    ➞ "Omtay otgay away mallsay iecepay ofway iepay."
    
    pig_latin("He told us a very exciting tale.")
    ➞ "Ehay oldtay usway away eryvay excitingway aletay."

### Notes

Be sure to preserve proper capitalization and punctuation.

"""

#Move the first letter of each word to the end of the word.
#Add "ay" to the end of the word.
#Words starting with a vowel (A, E, I, O, U) simply have "WAY" appended to the end.
​
lv = "aeiou"
uv = "AEIOU"
​
def piglatinize_word(word):
  if word=="": return ""
  y = ""
  capital = word[0].isupper()
  starting_with_v = word[0] in lv+uv
  if starting_with_v: y+=word[0]
  y += word[1:]
  if starting_with_v: y+="way"
  else: y+=word[0]+"ay"
  if capital: y = y.capitalize()
  return y
​
def pig_latin(txt):
  y = ""
  send = ""
  for c in txt:
    if c.isalpha(): send += c
    else:
      y += piglatinize_word(send)
      send = ""
      y += c
  return y

