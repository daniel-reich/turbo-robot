"""


Create a function that, given a **string** with at least **three characters**
, returns an array of its:

  1. Length.
  2. First character.
  3. Last character.
  4. Middle character, if the string has an odd number of characters. Middle TWO characters, if the string has an even number of characters.
  5. Index of the second occurrence of the second character in the format **"@ index #"** and **"not found"** if the second character doesn't occur again.

### Examples

    all_about_strings("LASA") ➞ [4, "L", "A", "AS", "@ index 3"]
    
    all_about_strings("Computer") ➞ [8, "C", "r", "pu", "not found"]
    
    all_about_strings("Science") ➞ [7, "S", "e", "e", "@ index 5"]

### Notes

N/A

"""

def all_about_strings(txt):
    L, FC,LC = len(txt), txt[0],txt[-1] #len, first, second
    #Midle
    if len(txt)%2==1:
        M = txt[len(txt)//2]
    else:
        M= txt[(len(txt)//2)-1:(len(txt)//2)+1]    
    return [L,FC,LC,M,second(txt)]
    
def second(X):
    N = list(enumerate(X))
    L =[]
    for inx,s in N:
        if s==X[1]:
            L.append(inx)
    if len(L)>=2:
        return '@ index {}'.format(L[-1])
    else:
        return "not found"

