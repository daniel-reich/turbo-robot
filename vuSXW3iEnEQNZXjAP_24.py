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
  try:
    start = '#'*l
    end = '\n' + '#'*l if l > 1 else ''
    mid = '\n#' + ' '*(l-2) + '#'
    return start + mid*(l-2) + end
  except: 
    return ''

