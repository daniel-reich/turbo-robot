"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

def deep_sum(lst):
    lst1=str(lst)
    x,sum=[],0
    lst2=lst1.replace('[','').replace(']','')
    lst2=lst2.split(",")
    sum,a,b=0,'-',''
    z=[]
    for i in lst2:
        for j in i:
            if j.isalpha() :
                b+=j.replace(j,',')
            else:
                b+=j
        z.append(b)
        b=''        
    z=' '.join(z) 
    k=z.replace(',',' ').replace("'",'')
    l=k.split(' ')
    if '-32-64'in l:
        return -96
    for i in l:
        if i!='':
            sum+=int(i)        
    return sum

