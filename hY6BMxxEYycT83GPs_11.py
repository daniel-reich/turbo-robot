"""


Given a **positive** number as a string, multiply the number by **11** and
also return it as a **string**. However, there is a catch:

 **You are NOT ALLOWED to simply cast the number into an integer!**

Now, how is this challenge even possible? Despite this, there is still a way
to solve it, and it involves thinking about how someone might multiply by 11
in their head. See the tips below for guidance.

### Examples

    multiply_by_11("11") ➞ "121"
    
    multiply_by_11("111111111") ➞ "1222222221"
    
    multiply_by_11("9473745364784876253253263723") ➞ "104211199012633638785785900953"

### Tip

There is a simple trick to multiplying any two-digit number by 11 in your
head:

  1. Add the two digits together
  2. Place the sum between the two digits!
  3. Note if the total goes over, carry the sum on to the next digit

    # 23 * 11
    # Add together 2 and 3 to make 5
    # Place 5 between the two digits to make 253
    # 77 * 11
    # Add together 7 and 7 to make 14
    # Place 4 between the two digits to make 747
    # Carry the 1 to make 847

### Notes

  * See [this resource](https://trachtenbergspeedmath.com/multiplication/basic-multiplication/multiplying-by-eleven/) to find out how this process can be utilized for numbers of any length!
  * This challenge was heavily inspired by [Mubashir Hassan's challenge](https://edabit.com/challenge/aHGLnfW7xdMrhJZpo) on adding two numbers together!

"""

def multiply_by_11(n):
    n = '0'+n+'0'
    n = n[::-1]
    retnum = ''
    carry = 0
    for i in range(len(n)-1):
        summ = int(n[i]) + int(n[i+1]) + carry
        if summ >= 10:
            carry = int(str(summ)[0])
            summ = int(str(summ)[1])
        else:
            carry = 0
        retnum = str(summ) + retnum
    if carry == 1:
        retnum = '1'+retnum
    return retnum

