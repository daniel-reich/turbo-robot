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
  sylabs = []
  while len(word) > 0:
    regex1 = r"(([^aeiou][aeiouy]+)([^aeiou][aeiouy]+))|(([^aeiou][aeiouy]+[^aeiou])([^aeiou][aeiouy]+))|(([^aeiou][aeiouy]+[^aeiou])([^aeiou]{2}[aeiouy]+))"
    regex2 = r"([^aeiou]{0,2}[aeiouy]{1,3}([^aeiou](?=[^aeiou]{2})|[^aeiou]?$|[^aeiou]??))"
    regex = regex1 + "|" + regex2
    syl = re.match(regex,word).groups()
    if syl[-2] is not None:
      sylabs.append(syl[-2])
      word = word[len(syl[-2]):]
    elif syl[1] is not None:
      sylabs.append(syl[1])
      word = word[len(syl[1]):]
    elif syl[4] is not None:
      sylabs.append(syl[4])
      word = word[len(syl[4]):]
    elif syl[7] is not None:
      sylabs.append(syl[7])
      word = word[len(syl[7]):]
  mod_sylabs = []
  for sylab in sylabs:
    if re.match(r"^([^aeiou])([^aeiou])([aeiouy])", sylab):
      sylab = re.sub(r"^([^aeiou])([^aeiou])([aeiouy])",r"\2\3\1",sylab, count=1)
    else:
      sylab = re.sub(r"^([^aeiou])([aeiouy])",r"\2\1",sylab, count=1)
    mod_sylabs.append(sylab)
  return "".join(mod_sylabs)

