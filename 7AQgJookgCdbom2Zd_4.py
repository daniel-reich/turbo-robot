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

def pig_latin(txt):
  txtList = txt.split()
  tempPunc = txtList[-1][-1]
  txtList[-1] = txtList[-1][:-1]
  #Removes the period from the last word in the list of words
  newString = ""
  temp = ""
  
  #Converts each word to pig latin
  for i in range (len(txtList)):
    if txtList[i][0] in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
      txtList[i]+="way"
    else:
      txtList[i].lower()
      temp = txtList[i][0]
      txtList[i] = txtList[i][1:]
      txtList[i]+= temp + "ay"
    
  #Capitalizes the first letter of the first word
  txtList[0] = txtList[0].capitalize()    
  
  #Adds all pig latin words into new string
  for i in range (len(txtList)):
    newString+=txtList[i] + " "
    
  newString = newString[:-1]
  newString+=tempPunc
  
  return newString

