"""


Someone has attempted to censor my strings by replacing every vowel with a
`*`, `l*k* th*s`. Luckily, I've been able to find the vowels that were
removed.

Given a censored string and a string of the censored vowels, return the
original uncensored string.

### Example

    uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
    
    uncensor("abcd", "") ➞ "abcd"
    
    uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

### Notes

  * The vowels are given in the correct order.
  * The number of vowels will match the number of `*` characters in the censored string.

"""

def uncensor(txt, vowels):
  for i in range(len(vowels)):
      txt=txt.replace('*',vowels[i],1)
  return txt

