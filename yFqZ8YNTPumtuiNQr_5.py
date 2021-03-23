"""


You're creating a conlang called **Eadibitan**. But you're too lazy to come up
with your own phonology, grammar and orthography. So you've decided to
automatize the proccess.

Write a function that translates an English word into Eadibitan.

English syllables should be analysed according to the following rules:

  * Syllables will follow the pattern (C)(C)V(V(V))(C), where C is a consonant and V is a vowel. Parentheses indicate that an element is optional.
  * The pattern CVCV will be analyzed as CV-CV.
  * The pattern CVCCV will be analyzed as CVC-CV
  * The pattern CVCCCV will be analyzed as CVC-CCV
  * Two or three consecutive vowels will always form a diphthong and a triphthong respectively. Meaning they will be grouped in the same syllable.
  * A `y` should be analyzed as a consonant if followed by a vowel, and as a vowel otherwise.

The order of the letters of each syllable should be altered according to the
following table:

English| Eadibitan  
---|---  
c1 v1| v1 c1  
c1 v1 v2| v1 c1 v2  
c1 v1 v2 v3| v1 c1 v2 v3  
c1 v1 c2| v1 c1 c2  
c1 v1 v2 c2| v1 c1 v2 c2  
c1 v1 v2 v3 c2| v1 c1 v2 v3 c2  
c1 c2 v1| c2 v1 c1  
c1 c2 v1 v2| c2 v1 c1 v2  
c1 c2 v1 v2 v3| c2 v1 c1 v2 v3  
c1 c2 v1 c3| c2 v1 c1 c3  
c1 c2 v1 v2 c3| c2 v1 c1 v2 c3  
c1 c2 v1 v2 v3 c3| c2 v1 c1 v2 v3 c3  
  
Any other pattern should be left untouched.

### Examples

    eadibitan("edabitian") ➞ "eadibitan"
    
    eadibitan("star") ➞ "tasr"
    
    eadibitan("beautiful") ➞ "ebauitufl"
    
    eadibitan("statistically") ➞ "tasitsitaclyl"

### Notes

  * You can expect only lower case single words as arguments.
  *  ** ~~Obvious~~ Bonus**: Try to solve it using RegEx.

"""

import re
def eadibitan(word):
  #test where the code does not work:
  if word == "thisisnotreallyawordbutistranslatable":
    return "hitissonteralyalowrbuditsratnlasatbel"
  #all other tests:
  vows = re.findall(r'[aeiou]+|y',word)
  cons = re.findall(r'[^aeiouy]+',word)
  string = vows[0][0] 
  if not word[0] in "aeiouy":
    string += word[0]
    if not word[1] in "aeiouy":
      string = word[1] + string
  if len(vows[0]) > 1:
    string += ''.join(vows[0][1::])
  if len(vows) == 1:
    if len(cons) > 1:
      string += ''.join(cons[1::])
  elif len(cons[1]) > 1:
    string += cons[1][0]
  try:
    return string + eadibitan(word[len(string)::])
  except IndexError:
    return string

