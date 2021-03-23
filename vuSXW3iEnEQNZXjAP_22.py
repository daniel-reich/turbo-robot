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
    if length is None or length < 1:
        return ''
    elif length == 1:
        return '#'
    return '\n'.join('#{}#'.format(('#' if i == 0 or i == length - 1 else ' ')
                                   * (length - 2))
                     for i in range(length))

