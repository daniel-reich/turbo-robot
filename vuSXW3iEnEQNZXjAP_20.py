"""


Create a function that takes a number and returns a string like square.

### Examples

    create_square(-1) ➞ ""
    
    create_square(0) ➞ ""
    
    create_square(1) ➞ "#"
    
    create_square(2) ➞ "##\n##"
    
    create_square(3) ➞ "###\n# #\n###"
    
    create_square(4) ➞ "####\n#  #\n#  #\n####"
    "####
    #  #
    #  #
    ####"

### Notes

N/A

"""

def create_square(n):
  arr = []
  if n==None or n <= 0:
    return ''
  elif n == 1:
    return '#'
  else:
    arr.append(n*'#')
    for i in range(n-2):
      arr.append('#'+(' '*(n-2)+ '#'))
    arr.append(n*'#')
  return '\n'.join(arr)

