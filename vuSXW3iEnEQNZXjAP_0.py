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
  if not n or n < 1:
    return ''
  elif n == 1:
    return '#'
  else:
    top = ['#'*n]
    bot = ['#'*n]
    mid = ['#' + ' '*(n-2) + '#'] * (n-2)
    return '\n'.join(top+mid+bot)

