"""


Write two functions:

  1. One to retrieve all **unique** substrings that **start** and **end** with a **vowel**.
  2. One to retrieve all **unique** substrings that **start** and **end** with a **consonant**.

The resulting array should be sorted in lexicographic ascending order (same
order as a dictionary).

### Examples

    get_vowel_substrings("apple")
    ➞ ["a", "apple", "e"]
    
    get_vowel_substrings("hmm") ➞ []
    
    get_consonant_substrings("aviation")
    ➞ ["n", "t", "tion", "v", "viat", "viation"]
    
    get_consonant_substrings("motor")
    ➞ ["m", "mot", "motor", "r", "t", "tor"]

### Notes

  * Remember the output array should have **unique** values.
  * The word itself counts as a potential substring.
  * Exclude the empty string when outputting the array.

"""

def func(txt,vowel:bool):  # txt for text; set vowel=True for get_vowel / False otherwise 
  out=[]
  print(txt)
  for x in range(0,len(txt)):
    if (txt[x] in ['a','e','i','o','u']) == vowel:
#     print(x,":",txt[x])
      for y in range(x,len(txt)):
#       print(x,y,txt[x:y+1])
        if (txt[y] in ['a','e','i','o','u']) == vowel:
          out.append(txt[x:y+1])
  out=list(set(out))   # transform to set to be unique
  out.sort()
  return(out)
​
def get_vowel_substrings(txt):
  return(func(txt,True))
​
def get_consonant_substrings(txt):
  return(func(txt,False))

