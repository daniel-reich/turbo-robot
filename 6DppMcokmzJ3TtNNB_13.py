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

def true_alphabetic(txt):
  x  = [len(i) for i in txt.split(" ")]
  txt = txt.replace(" ", "")
  print (x)
  y = sorted(txt, key=lambda x:ord(x))
  a = []
  print (y)
  b = ""
  p = 0
  for i in y:
    if x[p] == len(b):
      a.append(b)
      b = ""
      b += i
      p += 1
    else:
      b += i
  a.append(b)
  return " ".join(a)

