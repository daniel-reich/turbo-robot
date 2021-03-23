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
  if not isinstance(length,int) or length<1:
    return ''
  ret = ''
  if length>1:
    ret+=('#'*length)+'\n'
  for i in range(2,length):
    ret+='#'+(' '*(length-2))+'#\n'
  if length>0:
    ret+='#'*length
  return ret

