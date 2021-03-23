"""


Given two strings comprised of `+` and `-`, return a new string which shows
how the two strings interact in the following way:

  * When positives and positives interact, they _remain positive_.
  * When negatives and negatives interact, they _remain negative_.
  * But when negatives and positives interact, they _become neutral_ , and are shown as the number `0`.

### Worked Example

    neutralise("+-+", "+--") ➞ "+-0"
    # Compare the first characters of each string, then the next in turn.
    # "+" against a "+" returns another "+".
    # "-" against a "-" returns another "-".
    # "+" against a "-" returns "0".
    # Return the string of characters.

### Examples

    neutralise("--++--", "++--++") ➞ "000000"
    
    neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"
    
    neutralise("-++-", "-+-+") ➞ "-+00"

### Notes

The two strings will be the same length.

"""

neutralise=lambda a,b:"".join(["0",x][x==y]for x,y in zip(a,b))

