"""


Create a function which _simplifies_ a given **fraction** into its **simplest
ratio**. Return the fraction as a _string_.

### Examples

    simplify_frac("2/4") ➞ "1/2"
    
    simplify_frac("15/25") ➞ "3/5"
    
    simplify_frac("4/9") ➞ "4/9"

### Notes

  * Fractions are given as strings.
  * Return the same fraction if it is already in its simplified ratio (see example #3).

"""

def simplify_frac(string):
    return ["{}/{}".format(int(int(string.split('/')[0])/[e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i]),int(int(string.split('/')[1])/[e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i])) for i in range(-1,-len([e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0])-1,-1) if [e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i] in [e for e in range(1,int(string.split('/')[1])+1,1) if int(string.split('/')[1]) % e == 0]][0]

