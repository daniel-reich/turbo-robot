"""


Given a `fraction` (given in the format "1/2" for example) and `n` number of
decimal places, return a sentence in the following format:

 **"{fraction} rounded to {n} decimal places is {answer}"**

###  Examples

    frac_round("1/3", 5) ➞ "1/3 rounded to 5 decimal places is 0.33333"
    
    frac_round("2/8", 4) ➞ "2/8 rounded to 4 decimal places is 0.2500"
    
    frac_round("22/7", 2) ➞ "22/7 rounded to 2 decimal places is 3.14"

### Notes

  * Add trailing zeros if `n` is greater than the actual number of decimal places the fraction has (see example #2).
  * Numbers greater than one may be given as top-heavy fractions (no mixed numbers).
  * `n` won't be 1 because that would cause _"decimal places"_ to be _"decimal place"_ , making the challenge more cumbersome than it needs to be.

"""

def frac_round(frac, n):
  lst=frac.split('/')
  a='{0:.{b}f}'.format(round(int(lst[0])/int(lst[1]),n),b=n)
  return "{} rounded to {} decimal places is {}".format(frac,str(n),a)

