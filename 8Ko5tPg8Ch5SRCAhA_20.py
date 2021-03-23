"""


Create a function that, given a number, returns the corresponding value of
that index in the Fibonacci series.

The Fibonacci Sequence is the series of numbers:

    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding the two numbers before it:

  * The 2 is found by adding the two numbers before it (1+1).
  * The 3 is found by adding the two numbers before it (1+2).
  * The 5 is (2+3), and so on!

### Examples

    fibonacci(3) ➞ 3
    
    fibonacci(7) ➞ 21
    
    fibonacci(12) ➞ 233

### Notes

The first number in the sequence starts at 1 (not 0).

"""

def fibonacci(num):
    fbnc_dct = {}
​
    i = 0
    num = num + 2
​
    while i < num:
        if i == 0:
            fbnc_dct[i] = 0
        elif i == 1:
            fbnc_dct[i] = 1
        else:
            fbnc_dct[i] = fbnc_dct[i-1] + fbnc_dct[i-2]
​
        i += 1
​
    return fbnc_dct[num - 1]

