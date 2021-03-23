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
  it = 0
  ans = ''
  for i in txt:
    if i == '*':
      ans += vowels[it]
      it += 1
    else:
      ans += i
  return ans

