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
    '''
    Returns a string which can be printed out as a square of dimension n as per
    the instructions
    '''
    if n is None: return ''
    return '\n'.join('#'*n if i==1 or i==n else '#'+' '*(n-2)+'#'
                     for i in range(1,n+1))

