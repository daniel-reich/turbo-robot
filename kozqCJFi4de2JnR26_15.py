"""


A Fibonacci string is a precedence of the Fibonacci series. It works with any
two characters of the English alphabet (as opposed to the numbers `0` and `1`
in the Fibonacci series) as the initial items and concatenates them together
as it progresses in a similar fashion as the Fibonacci series.

### Examples

    fib_str(3, ["j", "h"]) ➞ "j, h, hj"
    
    fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"
    
    fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

### Notes

  * All values for `n` will be at least `2`.
  * A recursive version of the challenge can be found in [here](https://edabit.com/challenge/H7Z8enQWipfBMXTx7).

"""

# Hello World program in Python
    
def fib_str(n, txt):
    my_word = ""
    my_list = []
    my_list.append(txt[0])
    my_list.append(txt[1])
    my_word+=txt[0]+","+" "+txt[1]
    if (n == 2):
        my_word = txt[0]+","+" "+txt[1]
        return my_word
    elif (n>2):
        for i in range (2,n):
            my_list.append(my_list[i-1]+my_list[i-2])
    for i in range (2,len(my_list)):
        my_word+=","+" "+my_list[i]
    return my_word
txt = ["n","k"]
print(fib_str(6,txt))

