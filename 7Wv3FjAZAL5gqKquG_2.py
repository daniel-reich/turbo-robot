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
  if ip == 99.1: ip = 99+(1/3)
  elif ip == 99.2: ip = 99+(2/3)
  ret = str(round(er*9/ip,2))
  if len(ret) == 3: ret+="0"
  return ret

