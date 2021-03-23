"""


Write a function that takes two numbers, boundaries of a range, and returns a
list of functions which calculate the following:

    # n1 <= k < n2
    # if k – even, then f(x) = x + k
    # if k –  odd, then f(x) = x * k

### Examples

    f1, f2 = make_fun_lst(5, 7)
    print((f1(4), f2(14))) ➞ (20, 20)

### Notes

This question is from an evaluation procedure at an interview. A person who
can solve this without thinking has expertise in Python above the intermediate
level.

"""

make_fun_lst=lambda f,l:[eval("lambda x,_=i:x%s_"%("*"if i%2else "+"))for i in range(f,l)]

