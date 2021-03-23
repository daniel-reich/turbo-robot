"""


Given a _pH value_ , return whether that value is `"alkaline"` (greater than
7), `"acidic"` (less than 7), or `"neutral"` (7). Return `"invalid"` if the
value given is **less than 0** or **greater than 14**.

![Image of a pH chart](https://edabit-
challenges.s3.amazonaws.com/color_spec.png)

### Examples

    pH_name(5) ➞ "acidic"
    
    pH_name(8.7) ➞ "alkaline"
    
    pH_name(7) ➞ "neutral"

### Notes

Values such as 6.9999 and 8.00001 should return `"acidic"` and `"alkaline"`
respectively.

"""

def pH_name(pH):
  if pH > 0 and pH < 7: return 'acidic' 
  if pH >= 7 and pH < 8: return 'neutral'
  if pH > 7 and pH <= 14: return 'alkaline'
  return 'invalid'

