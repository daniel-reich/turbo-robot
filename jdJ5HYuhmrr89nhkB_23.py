"""


Write a function that returns a **lambda expression** , which adds `n` to its
input

### Examples

    adds1 = adds_n(1)
    
    adds1(3) ➞ 4
    adds1(5.7) ➞ 6.7
    
    adds10 = adds_n(10)
    
    adds10(44) ➞ 54
    adds10(20) ➞ 30

### Notes

N/A

"""

def adds_n(n):
  return lambda number_to_add : number_to_add + n

