"""


Create a function that takes a string and returns **dashes** on both sides of
every vowel ( _a e i o u_ ).

### Examples

    dashed("Edabit") ➞ "-E-d-a-b-i-t"
    
    dashed("Carpe Diem") ➞ "C-a-rp-e- D-i--e-m"
    
    dashed("Fight for your right to party!") ➞ "F-i-ght f-o-r y-o--u-r r-i-ght t-o- p-a-rty!"

### Notes

  * A string can contain uppercase and lowercase vowels.
  *  **Y** is not considered a vowel.

"""

def dashed(txt):
  vows = "aeiouAEIOU"
  arr = []
  for c in txt:
    if c in vows:
      arr.append("-{0}-".format(c))
    else : arr.append(c)
  return "".join(arr)

