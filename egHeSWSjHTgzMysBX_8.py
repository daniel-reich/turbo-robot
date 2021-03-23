"""


Create a function that takes a number as an argument and returns half of it.

### Examples

    half_a_fraction("1/2") ➞ "1/4"
    
    half_a_fraction("6/8") ➞ "3/8"
    
    half_a_fraction("3/8") ➞ "3/16"

### Notes

Always return the simplified fraction.

"""

def half_a_fraction(fract):
    fract = list(map(lambda x:int(x), fract.split('/')))
    if (fract[0]) % 2 == 0:
        fract[0] = str(int(fract[0]/ 2))
    else:
        fract[1] = str(fract[1]* 2)
    fract = list(map(lambda x:str(x), fract))
    return '/'.join(fract)

