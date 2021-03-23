"""


Create a function that returns the average of a list composed of letters.
First, find the number of the letter in the alphabet in order to find the
average of the list.

    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    average = total sum of all numbers / number of item in the set

Return the result rounded to two decimal points.

### Examples

    average_index(["a", "b", "c", "i"]) ➞ 3.75
    
    average_index(["e", "d", "a", "b", "i", "t"]) ➞ 6.83
    
    average_index(["y", "o", "u", "a", "r", "e", "t", "h", "e", "b", "e", "s", "t"]) ➞ 12.62

### Notes

N/A

"""

def average_index(letters):
  letr_dict = {chr(i): i-96 for i in range(97, 97 + 26)}
  result = [letr_dict[i] for i in letters]
  return round(sum(result) / len(letters),2)

