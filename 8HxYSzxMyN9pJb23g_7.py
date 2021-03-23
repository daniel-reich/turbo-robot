"""


Create a function that accepts `txt` and `cases` as parameters where the
string is split into **N distinct cases** of **equal length** as shown:

### Examples

    split_n_cases("Strengthened", 6) ➞ ["St", "re", "ng", "th", "en", "ed"]
    
    split_n_cases("Unscrupulous", 2) ➞ ["Unscru", "pulous" ]
    
    split_n_cases("Flavorless", 1) ➞ ["Flavorless" ]

### Notes

If it's not possible to split the string as described, return `["Error"]`.

"""

def split_n_cases(txt, cases):
  if len(txt)%cases==0:
    n=int(len(txt)/cases)
    return [txt[i:i+n] for i in range(0,len(txt), n)]
  else:
    return [ "Error" ]

