"""


Create a function that can turn Yen (Japanese dollar) to USD (American
dollar).

### Examples

    yen_to_usd(1) ➞ 0.01
    
    yen_to_usd(500) ➞ 4.65
    
    yen_to_usd(649) ➞ 6.04

### Notes

  * Each Yen to USD conversion is Yen / 107.5
  * Round the result to two decimal places.

"""

def yen_to_usd(yen):
  ans = yen / 107.5
  return  round(ans,2)

