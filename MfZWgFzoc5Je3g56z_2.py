"""


Create a function that takes two numbers as an argument and returns the
minimum number of steps that we need to do inside a range of numbers to obtain
a secret number.

The first number, `ran`, allow us to define the range of numbers that will be
used to determine the secret number. The range runs from `0` up to `ran**2`
(the number `ran**2` is part of the range).

The second number, `num`, is the number we will use to determine the secret
number. The secret number will be the mirror of `num` in the range previously
defined.

Finally, we need to determine the minimum number of steps we need to do from
`num` to the secret number. We can move forward of backwards through the
range.

### Examples

    translate(3, 0) ➞ "-1 ---> 9"
    # Here the range of numbers will be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
    # The secret number will be 9, since 9 is the mirror of 0 in the defined range.
    # The minimum number of steps to go from 0 to 9 is -1 (-1 < 9, being 9 the
    # number of required steps if we move forward).
    
    translate(3, 2) ➞ "+5 or -5 ---> 7"
    # In this case, we can move to the secret number doing 5 setps forward or 5
    # steps backwards, starting from 2.
    
    translate(3, 4) ➞ "+1 ---> 5"
    
    translate(9, 100) ➞ "100 is not in the range [0:81]"
    
    translate(10, 50) ➞ "+0 ---> 50"

### Notes

N/A

"""

def translate(ran, num):
    if num < 0 or num > ran**2:
        return str(num) + ' is not in the range [0:' + str(ran**2) + ']'
    secret = ran**2 - num
    steps1 = abs(num - secret)
    steps2 = ran**2 - max(secret, num) + min(secret, num) + 1
    if steps1 < steps2:
        if num > secret:
            ans = '-' + str(steps1)
        else:
            ans = '+' + str(steps1)
    elif steps2 < steps1:
        if num > secret:
            ans = '+' + str(steps2)
        else:
            ans = '-' + str(steps2)
    else:
        ans = '+' + str(steps1) + ' or -' + str(steps2)
    ans += ' ---> ' + str(secret)
    return ans

