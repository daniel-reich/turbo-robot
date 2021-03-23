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

def create_square(l):
  if l == 1 : return '#'
  return '' if not l or l<1 else '#'*l+('\n#'+' '* (l-2)+'#')*(l-2)+'\n'+'#'*l

