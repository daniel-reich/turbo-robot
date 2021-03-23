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
  if length == None or length <= 0:
    return ""
  elif length == 1:
    return "#"
  elif length == 2:
    return "##\n##"
  else:
    return "\n".join(["#"*length, "\n".join(["#" + " "*(length-2) + "#"  for i in range(length - 2)]), "#"*length])

