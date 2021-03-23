"""


Create a function that takes a list as an argument and returns a new nested
list for each element in the original list. The nested list must be filled
with the corresponding element (string or number) in the original list and
each nested list has the same amount of elements as the original list.

### Examples

    multiply([4, 5]) ➞ [[4, 4], [5, 5]]
    
    multiply(["*", "%", "$"]) ➞ [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]]
    
    multiply(["A", "B", "C", "D", "E"]) ➞ [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]]

### Notes

The given list contains numbers or strings.

"""

def multiply(l):
  big_list = []
  for i in l:
    i_list = []
    for j in range(0,len(l)):
      i_list.append(i)
    big_list.append(i_list)
  return big_list

