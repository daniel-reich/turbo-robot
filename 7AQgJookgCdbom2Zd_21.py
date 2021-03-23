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
    txt1 = ""
    for i in txt:
        if i.isalpha() or i is ' ':
            txt1 = txt1 + i
​
    vowels = "aeiouAEIOU"
    listy = []
    splitty = txt1.split()
​
    for i in splitty:
        if i[0] in vowels:
            listy.append(i+'way')
        else:
            listy.append(i[1::] + i[0:1:]+'ay')
​
    firsty = listy[0].capitalize()
​
    list2 = []
    list2.append(firsty)
    for i in listy[1::]:
        list2.append(i)
    stringy =  (' '.join(list2))
    return stringy+txt[-1]

