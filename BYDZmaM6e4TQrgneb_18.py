"""


In mathematics, the **Fibonacci numbers** , commonly denoted **Fn** , form a
sequence, called the Fibonacci sequence, such that each number is the sum of
the two preceding ones, starting from 0 and 1:

![Fibonacci Sequence](https://edabit-
images.s3.amazonaws.com/3c667d91153450b3a161371582ee8227af85951f.svg)

and

![Fibonacci Sequence 2](https://edabit-
images.s3.amazonaws.com/0fff1a1716fcc169546079870357f92757ade5fa.svg)

for n > 1

The beginning of the sequence is thus:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

The function **fastFib** (num) returns the fibonacci number **Fn** , of the
given `num` as an argument.

### Examples

    fib_fast(5) ➞ 5
    
    fib_fast(10) ➞ 55
    
    fib_fast(20) ➞ 6765
    
    fib_fast(50) ➞ 12586269025

### Notes

  * The input number is always positive.
  * You have to make it **Fast**.

"""

def fib_fast(num):
  fnMin1 = 1
  fnMin2 = 0
  fn = 1
  temp = 0
  if num == 0:
    return 0
  elif num == 1:
    return 1
  for i in range(2,num):
    #print (fnMin2, fnMin1, fn, i)
    temp = fn   
    fnMin2 = fnMin1
    fnMin1 = temp
    fn = fnMin1 + fnMin2
  return fn

