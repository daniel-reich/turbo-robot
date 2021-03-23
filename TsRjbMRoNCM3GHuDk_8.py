"""


The syllabic structure of Persian language is CV(C)(C). C stands for
consonants and V stands for Vowels. The CV(C)(C) means that there are three
types of syllables in Persian:

  * CV
  * CVC
  * CVCC

Write a function that takes the phonetic transcription of a Persian word as an
argument and returns the syllabified word based on the syllabic structure. In
other word, put a period between syllables.

### Examples

    syllabification("kAr") ➞ "kAr"
    
    syllabification("bArAn") ➞ "bA.rAn"
    
    syllabification("tA") ➞ "tA"
    
    syllabification("deraxt") ➞ "de.raxt"
    
    syllabification("pust") ➞ "pust"
    
    syllabification("lAjevard") ➞ "lA.je.vard"

### Notes

  * Mono-syllabic words don't need syllabification.
  * Persian has six vowels: `a, A, e, i, o, u`
  * Persian has 23 consonants: `p, b, t, d, k, g, G, ?, f, v, s, z, S, Z, x, h, c, j, m, n, r, l, y`
  * Try to solve the problem by using RegEx.

### Hint

Since each syllable has only one vowel, it's not necessary to know the
consonants. Just knowing that there are only one consonant before the vowel
and 0 to 2 consonants after the vowel is enough to solve the challenge.

"""

def syllabification(word):
​
  vowels = 'a, A, e, i, o, u'.split(', ')
  vowel_indexes = []
​
  for n in range(len(word)):
    l8r = word[n]
    if l8r in vowels:
      vowel_indexes.append(n)
  
  if len(vowel_indexes) == 0:
    return word
​
  section_beginnings = {}
​
  for index in vowel_indexes:
    section_beginnings[index] = index - 1
  
  section_endings = {}
​
  for n in range(len(vowel_indexes) - 1):
    index = vowel_indexes[n]
    backstop = section_beginnings[vowel_indexes[n+1]]
​
    section_endings[index] = backstop
​
  sections = []
​
  for index in vowel_indexes:
    
    start = section_beginnings[index]
    try: 
      end = section_endings[index]
    except KeyError:
      end = None
    
    if end == None:
      sections.append(word[start:])
    else:
      sections.append(word[start:end])
  
  return '.'.join(sections)

