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
    r = []
    if length == None or length < 1:
        return ""
    for i in range(length):
        if i == 0 or i == length - 1:
            r.append("#" * length)
        else:
            r.append("#" + " " * (length - 2) + "#")
    return "\n".join(r)

