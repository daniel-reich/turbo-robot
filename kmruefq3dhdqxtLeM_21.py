"""
Create a function that sums the total number of digits between two numbers,
**inclusive**. For example, between the numbers `19` and `22` we have:

    # 19, 20, 21, 22
    (1 + 9) + (2 + 0) + (2 + 1) + (2 + 2) = 19

### Examples

    sum_digits(7, 8) ➞ 15
    
    sum_digits(17, 20) ➞ 29
    
    sum_digits(10, 12) ➞ 6

### Notes

N/A

"""

def sum_digits(a, b):
  def digit_sum(number):
    return sum([int(digit) for digit in str(abs(number))])
  return sum([digit_sum(number) for number in range(a,b+1)])

