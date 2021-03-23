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
  lst1 = [122-ord(character) for character in letters]
  lst2 = [26-i for i in lst1]
  return round(sum(lst2)/len(lst2),2)

