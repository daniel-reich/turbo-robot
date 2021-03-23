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
  def string(i,j):
    return "#" if min(i,j) == 0 or max(i,j) == length - 1 else " "
  if length is None:
    return ""
  elif length < 1:
    return ""
  else:
    s = ""
    for i in range(0,length):
      for j in range(0,length):
        s += string(i,j)
      if i < length - 1:
        s +="\n"
    return s

