"""


Write a function that swaps the first **pair** (1st and 2nd characters) with
the second **pair** (3rd and 4th characters) for every quadruplet substring.

### Examples

    swap_two("ABCDEFGH") ➞ "CDABGHEF"
    
    swap_two("AABBCCDDEEFF") ➞ "BBAADDCCFFEE"
    
    swap_two("munchkins") ➞ "ncmuinhks"
    
    swap_two("FFGGHHI") ➞ "GGFFHHI"

### Notes

Keep **leftover strings** in the same order.

"""

def swap_two(txt):
  arr=[]
  for i in txt:
    arr.append(i)
  a=0
  b=1
  c=2
  d=3
  temp=[]
  for i in range(len(arr)//4):
    temp=arr[a]
    arr[a]=arr[c]
    arr[c]=temp
    temp=arr[b]
    arr[b]=arr[d]
    arr[d]=temp
    a+=4
    b+=4
    c+=4
    d+=4
  s=""
  for i in arr:
    s+=i
  return s

