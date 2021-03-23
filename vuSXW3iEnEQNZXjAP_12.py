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

def create_square(le):
  if not le :
    le = -1
    return ''
  if le < 1 :
    return ''
  if le == 1:
    return "#"
  f,l = "#"*le+"\n","#"*le
  m = "#"+" "*(le-2)+"#\n"
  return (f+(m*(le-2))+l)

