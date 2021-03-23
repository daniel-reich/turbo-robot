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
  consonants = ['p','b','t','d','k','g','G','?','f','v','s', 
               'z','S','Z','x','h','c','j','m','n','r','l',
               'y']
  vowels, pos, out, p1, dotcount = ['a','A','e','i','o','u'],[],'',0,0
  pos = [i for i in range (len(word)) if word[i] in vowels]
  for i in range (len(pos)):
    if (i ==  len(pos)-1):
      out+=word[p1:]
    else:
      out+=word[p1:pos[i+1]-1]+'.'
      dotcount+=1
    p1= len(out)-dotcount
  return out

