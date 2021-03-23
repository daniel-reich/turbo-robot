"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
  string=str(num).replace('-','')
  lst=[int(string[i]+'0'*len(string[i+1:])) for i in range(len(string))]
  if num<0:
    return list(map(lambda x:-x,lst))
  return lst

