"""


Return the coordinates (`[row, col]`) of the element that differs from the
rest.

### Examples

    where_is_waldo([
      ["A", "A", "A"],
      ["A", "A", "A"],
      ["A", "B", "A"]
    ]) ➞ [3, 2]
    
    where_is_waldo([
      ["c", "c", "c", "c"],
      ["c", "c", "c", "d"]
    ]) ➞ [2, 4]
    
    where_is_waldo([
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["O", "O", "O", "O"],
      ["P", "O", "O", "O"],
      ["O", "O", "O", "O"]
    ]) ➞ [5, 1]

### Notes

  * The given list will always be a square.
  * Rows and columns are 1-indexed ( **not zero-indexed** ).

"""

def where_is_waldo(lst):
  locate = differ_char(lst)
  for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
      if lst[i][j] == locate:
        return [i+1,j+1]
  
​
def differ_char(lst):
  chars ={}
  for ele in lst:
    for char in ele:
      if char in chars:
        chars[char] +=1
      else:
        chars[char] =1
  if len(chars) !=1:
    locate =''
    for key,values in chars.items():
      if chars[key] == 1:
        locate = key
  return locate

