"""


A prime number is a number whose only proper (non-self) divisor is 1 (example
13).

An emirp (prime spelled backwards) is a non-palindromic prime which, when its
digits are reversed, makes _another_ prime. E.g. 13 is a prime, and so is 31.
Both are therefore emirps.

A bemirp is a prime which is an emirp (makes another prime with its digits
reversed), but additionally, makes another prime when flipped upside down (see
note). The upside-down version is also an emirp, which makes a group of 4
primes. Bemirps consist only of digits 0, 1, 6, 8, and 9.

To illustrate: 11061811, reversed = 11816011, upside-down = 11091811, upside-
down reversed = 11819011. All four are primes.

Create a function that takes a number and returns `"B"` if it’s a bemirp,
`"E"` if it's a (non-bemirp) emirp, `"P"` if it's a (non-emirp) prime, or
`"C"` (composite / non-prime).

### Examples

    bemirp(101) ➞ "P"
    
    bemirp(1011) ➞ "C"
    
    bemirp(1069) ➞ "E"
    
    bemirp(1061) ➞ "B"

### Notes

6 upside-down is 9 and vice-versa. 0, 1, and 8 are unchanged when flipped. The
remaining five digits are unflippable.

"""

# Helper Function - is prime
def is_prime(num):
 prime=True
 if num > 1:
  for i in range(2,num):
   if num % i == 0:
    prime=False
    break
 else:
  prime=False
 return prime
​
# Helper function - is emirp - prime backwards but no palindrome
def is_emirp(n):
 n_str=str(n)
 n_rev=n_str[-1::-1]
 #print('n_rev ',n_rev)
 if n_str != n_rev and is_prime(int(n_rev)):
  return True
 else:
  return False
 
​
# Function
def bemirp(n):
 # check if prime
 #  else "C"
 if is_prime(n):
  # check if emirp - prime backwards but no palindrome
  #  else "P"
  if is_emirp(n):
   # check if bemirp - then output "B"
   #  else "E"
   # check if contains non-flippable digits
   non_flip=['2','3','4','5','7']
   flippable=True
   for i in range(0,len(str(n))):
    if str(n)[i] in non_flip:
     output="E"
     flippable=False
     break
   #  if not, flip n
   if flippable:
    flip=""
    for k in range(0,len(str(n))):
     if str(n)[k] == '6':
      flip+='9'
     elif str(n)[k] == '9':
      flip+='6'
     else:
      flip+=str(n)[k]
    #print('flip ',flip)
    # if flip is prime
    #  check if emirp
    if is_prime(int(flip)) and is_emirp(int(flip)):
     output="B"    
    else:
     output="E"
  else:
   output="P"  
 else:
  output="C"
 return output

