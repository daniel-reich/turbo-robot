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
  try:
    if length <= 0:
      return ""
    elif length == 1:
      return "#"
    else:
      return "#"*length+"\n"+(length-2) * str("#"+" "*(length-2)+"#"+"\n")+ "#"*length
  except:
    return ""

