"""


Write a function that sorts list while keeping the list structure. Numbers
should be first then letters both in ascending order.

### Examples

    num_then_char([
      [1, 2, 4, 3, "a", "b"],
      [6, "c", 5], [7, "d"],
      ["f", "e", 8]
    ]) ➞ [
      [1, 2, 3, 4, 5, 6],
      [7, 8, "a"],
      ["b", "c"], ["d", "e", "f"]
    ]
    
    num_then_char([
      [1, 2, 4.4, "f", "a", "b"],
      [0], [0.5, "d","X",3,"s"],
      ["f", "e", 8],
      ["p","Y","Z"],
      [12,18]
    ]) ➞ [
      [0, 0.5, 1, 2, 3, 4.4],
      [8],
      [12, 18, "X", "Y", "Z"],
      ["a", "b", "d"],
      ["e", "f", "f"],
      ["p", "s"]
    ]

### Notes

Test cases will contain integer and float numbers and single letters.

"""

def num_then_char(lst):
  def seperator(lst):
    list_lengths = {}
    numbers = []
    l8rs = []
    for n in range(len(lst)):
      length = len(lst[n])
      list_lengths[n] = length
      for item in lst[n]:
        if isinstance(item, int) == True or isinstance(item, float) == True:
          numbers.append(item)
        else:
          l8rs.append(item)
    return list_lengths, numbers, l8rs
  def combiner(lengths, inputs):
    
    lsts = []
​
    for n in range(len(list(lengths.keys()))):
      
      lst = []
      count = 0
      goal = lengths[n]
​
      while count < goal:
        lst.append(inputs[0])
        inputs.pop(0)
        count += 1
      
      lsts.append(lst)
    
    return lsts
​
​
  s = seperator(lst)
​
  lengths = s[0]
  numbers = sorted(s[1])
  l8rs = sorted(s[2])
​
  inputts = numbers + l8rs
​
  c = combiner(lengths, inputts)
​
  return c

