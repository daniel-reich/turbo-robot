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
  if length == None or length < 1: return ""
  if length == 1: return "#"
  square = '#' * length + "\n"
  for x in range(1, length - 1):
    square += "#" + (" " * (length - 2)) + "#\n"
  square += "#" * length
  return square

