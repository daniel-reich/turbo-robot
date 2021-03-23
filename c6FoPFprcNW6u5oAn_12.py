"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def coprime(x, y):
    return gcd(x, y) == 1
    
def farey(n) :
  n = n+1
  #num and demnom must not have any common factors, num must be less than demon 
  #make a list of lists
  pretty_list = []
  calc_list = []
  for numer in range(n) :
    for demon in range(1,n) :
      if coprime(numer,demon) and demon > numer :
        #print(numer,'/',demon)
​
        calc_list += [[numer,demon]]
​
​
  sorted_clac_list = sorted(calc_list, key=lambda x: x[0]/x[1])
​
  pretty_list = []
  for i in sorted_clac_list :
    pretty_list += [str(i[0]) + '/' + str(i[1])]
​
  pretty_list += ['1/1']
​
  return pretty_list

