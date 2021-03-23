"""


Turn each character in a string `s` into its ASCII character code and join
them together to create a number.

For example, for string "abc", the number is 979899. We will call this number
"num1".

    "abc" ➞ "a" = 97, "b" = 98, "c" = 99 ➞ 979899

Then replace any incidence of the number 7 with the number 1, and call this
number "num2":

    num1 = 979899
    
    num2 = 919899

Return the difference between the sum of the digits in num1 and num2:

      (9 + 7 + 9 + 8 + 9 + 9)
    - (9 + 1 + 9 + 8 + 9 + 9)
    -------------------------
             ➞  6

### Examples

    calc("ABCDabcd") ➞ 12
    
    calc("cdefgh") ➞ 0
    
    calc("ifkhchlhfde") ➞ 6)

### Notes

Lowercase and uppercase characters have different ASCII character codes.

"""

def calc(s):
    num1 = ''
    num2 = ''
    sum1 = 0
    sum2 = 0
    for n in s:
        num1 += str(ord(n))
    for i in num1:
        if int(i) == 7:
            num2 += str(1)
        else:
            num2 += str(i)
    for l in num1:
        sum1 += int(l)
    for l in num2:
        sum2 += int(l)
    return sum1-sum2

