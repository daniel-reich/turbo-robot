"""


An _authentic_ vowel skewer is a skewer with a delicious and juicy mix of
consonants and vowels. However, the way they are made must be _just right_ :

  * Skewers must begin and end with a **consonant**.
  * Skewers must **alternate** between consonants and vowels.
  * There must be an **even spacing** between each letter on the skewer, so that there is a consistent flavour throughout.

Create a function which returns whether a given vowel skewer is **authentic**.

### Examples

    is_authentic_skewer("B--A--N--A--N--A--S") ➞ True
    
    is_authentic_skewer("A--X--E") ➞ False
    # Should start and end with a consonant.
    
    is_authentic_skewer("C-L-A-P") ➞ False
    # Should alternate between consonants and vowels.
    
    is_authentic_skewer("M--A---T-E-S") ➞ False
    # Should have consistent spacing between letters.

### Notes

  * All tests will be given in uppercase.
  * Strings without any actual skewer `"-"` or letters should return `False`.

"""

def is_authentic_skewer(s):
  
  l8rs = []
  seperators = set()
  seperator = ''
  print(s)
  for item in s:
    if item.isalpha() == True:
      l8rs.append(item)
      if seperator != '':
        seperators.add(seperator)
        seperator = ''
    elif item == '-':
      seperator += '-'
    else:
      print(item)
      return False
  
  if len(l8rs) == 0:
    return False
    
  if seperator != '':
    seperators.add(seperator)
  
  if len(list(seperators)) != 1:
    print(list(seperators))
    return False
  
  vowels = 'aeiou' + 'aeiou'.upper()
  
  for n in range(len(l8rs)):
    l8r = l8rs[n]
    even = n%2==0
    
    if even == True:
      if l8r in vowels:
        print('even-vowel')
        return False
    else:
      if l8r not in vowels:
        print('odd-con')
        return False
  
  if s.split(list(seperators)[0]) != l8rs:
    print(l8rs)
    return False
  
  return True

