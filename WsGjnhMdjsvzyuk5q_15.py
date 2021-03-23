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
  vowels  = ['a','e','i','o','u','A','E','I','O','U']
  lista = ['-{}-'.format(i)if i in vowels else i for i in txt ]
  return ''.join(lista)

