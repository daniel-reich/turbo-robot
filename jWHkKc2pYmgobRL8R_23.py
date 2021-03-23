"""


Write a function that takes in a string and for each character, returns the
distance to the nearest vowel in the string. If the character is a vowel
itself, return `0`.

### Examples

    distance_to_nearest_vowel("aaaaa") ➞ [0, 0, 0, 0, 0]
    
    distance_to_nearest_vowel("babbb") ➞ [1, 0, 1, 2, 3]
    
    distance_to_nearest_vowel("abcdabcd") ➞ [0, 1, 2, 1, 0, 1, 2, 3]
    
    distance_to_nearest_vowel("shopper") ➞ [2, 1, 0, 1, 1, 0, 1]

### Notes

  * All input strings will contain **at least one vowel**.
  * Strings will be lowercased.
  * Vowels are: `a, e, i, o, u`.

"""

def distance_to_nearest_vowel(txt):
  r=["a","e","i","o","u"]
  fi=[]
  c=0
  switch=False
  for t in range(len(txt)):
    if txt[t] in r:
      fi.append(0)
      c=0
      switch=True
    else:
      if switch==True:
        c+=1
      v=1
      if t==len(txt)-1:
        fi.append(c)
        break
      for y in txt[t+1:]:
        if y not in r:
          v+=1
        if y in r:
          break
      if c<v and switch==True:
        fi.append(c)
      else:
        fi.append(v)
      v=0
  return fi

