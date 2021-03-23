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
  x=txt
  a=[]
  fin=''
  for i in x:
    a.append(i)
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j] and a[i]!=' ' and a[j]!=' ':
        a[i],a[j]=a[j],a[i]
  for i in a:
    fin+=i
  return(fin)

