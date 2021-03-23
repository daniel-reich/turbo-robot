"""


 **Mubashir** was trying to understand [Divisibility
Rule](https://en.wikipedia.org/wiki/Divisibility_rule) on Wikipedia which
states :

 _"A divisibility rule is a shorthand way of determining whether a given
integer is divisible by a fixed divisor without performing the division,
usually by examining its digits."_

He came up with an important fact for **Divisibility by 13** rule on
Wikipedia, which states that if you divide the successive powers of **10 by
13** you get the following remainders :

    10^0 % 13 = 1
    10^1 % 13 = 10
    10^2 % 13 = 9
    10^3 % 13 = 12
    10^4 % 13 = 3
    10^5 % 13 = 4
    10^6 % 13 = 1 (repetition starts from here)

They concluded the following method:

  * Multiply the **right-most digit** of the number with the **left-most number** in the sequence shown above and the **second right-most digit** to the **second left-most digit** of the number in the sequence and so on.
  * Sum up all these products.
  * Repeat this process until the sum remains **constant**.

What is the remainder when `1234567` is divided by `13`?

    7      6     5      4     3     2     1  (digits of 1234567 from the right)
    ×      ×     ×      ×     ×     ×     ×  (multiplication)
    1     10     9     12     3     4     1  (repeating sequence)

We get:

    7×1 + 6×10 + 5×9 + 4×12 + 3×3 + 2×4 + 1×1 = 178

Repeat same process with `178`:

    8x1 + 7x10 + 1x9 = 87

Repeat same process with `87`:

    7x1 + 8x10 = 87 (repetition starts from here)

Create a function that processes this sequence of operations on the given
integer `n` and returns the final `constant` value.

### Examples

    divisibility_rule(1234567) ➞ 87
    
    divisibility_rule(8529) ➞ 79
    
    divisibility_rule(85299258) ➞ 31

### Notes

N/A

"""

class Divisibility_rule:
​
  ten_by_13 = [1, 10, 9, 12, 3, 4]
​
  def __init__(self, start):
    self.s = [start]
  
  def advance(self):
​
    number = list(reversed(str(self.s[-1])))
    nn = []
    index = 0
    for n in range(len(number)):
​
      try:
        nn.append(int(number[n]) * Divisibility_rule.ten_by_13[n])
      except IndexError:
        nn.append(int(number[n]) * Divisibility_rule.ten_by_13[index])
        index += 1
        if index >= len(Divisibility_rule.ten_by_13):
          index = 0
   #     print(index, int(number[n]), n, number, nn)
  #  print(sum(nn), self.s)
    self.s.append(sum(nn))
​
​
def divisibility_rule(n):
​
  dr = Divisibility_rule(n)
​
  while len(list(set(dr.s))) == len(dr.s):
    dr.advance()
  
  return dr.s[-1]

