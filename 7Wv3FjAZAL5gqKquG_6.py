"""
Create a function that returns an _Earned Run Average_ (ERA). An ERA is
calculated by multiplying **9** by the quotient of _Earned Runs Allowed_ `er`
divided by `ip` _Innings Pitched_.

In baseball statistics, _innings_ are represented with a fractional part of
**.1** (1/3) or **.2** (2/3) to represent the number of _outs_ in an inning. A
whole number or a number with a fractional part of **.0** represents a full
inning with three _outs_. Check the **Resources** tab for a deeper
explanation.

### Examples

    era(22, 99) ➞ 2.00
    
    era(23, 99.1) ➞ 2.08
    
    era(24, 99.2) ➞ 2.17

### Notes

  * ERA is represented with a scale of _2_ : **2.08**
  * For 1/3 and 2/3, use a scale of _2_.

"""

def era(er, ip):
  if ip % 1 == 0:
    return '%.2f' % (er/ip*9)
  remainder = ip % 1
  base = ip // 1
  remainder *= 3
  ip = base + remainder
  return '%.2f' % (er/ip*9)

