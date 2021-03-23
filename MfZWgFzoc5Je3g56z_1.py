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

import numpy as np
​
def translate(ran, num):
    np_sign = lambda x: "+" if np.sign(x)==1 or np.sign(x)==0 else '-'
​
    if num > ran**2:
        return str(num) + " is not in the range [0:" + str(ran**2) + "]"
    else:
        secret_number = ran**2-num
        num_one = secret_number - num
        if np.sign(num_one)==-1:
            num_two = num_one + (ran ** 2 + 1)
        else:
            num_two = num_one - (ran ** 2 + 1)
        if abs(num_one) < abs(num_two):
            return np_sign(num_one) + str(abs(num_one)) + " ---> " + str(secret_number)
        elif abs(num_one) > abs(num_two):
            return np_sign(num_two) + str(abs(num_two)) + " ---> " + str(secret_number)
        else:
            if np.sign(num_one)==-1:
                return np_sign(num_two) + str(abs(num_two)) + " or " + np_sign(num_one) + str(abs(num_one)) + " ---> " + str(secret_number)
            else:
                return np_sign(num_one) + str(abs(num_one)) + " or " + np_sign(num_two) + str(abs(num_two)) + " ---> " + str(secret_number)

