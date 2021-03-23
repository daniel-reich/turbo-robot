"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

def true_alphabetic(n):
  a = sorted(n.replace(" ", ""))
  b = ""
  c = 0
  for i in n:
      if i != " ":
          b += a[c]
          c += 1
      else: b += " "
  return b

