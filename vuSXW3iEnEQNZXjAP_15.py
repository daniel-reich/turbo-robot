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

def create_square(length):
  if type(length) != int:
    return "" 
  arr = []
  for i in range(length):
    if i == 0:
      arr.append('#'*length)
    elif i == length-1:
      arr.append('\n' + '#'*length)
    else : arr.append('\n'+'#' + ' '*(length-2) + '#')
  return "".join(arr)

