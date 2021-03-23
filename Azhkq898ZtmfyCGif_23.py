"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

def divide_list(lst, separator):
  if separator not in lst:
    return [lst]
  
  cuts = []
  for i in range(len(lst)):
    if lst[i] == separator:
      cuts.append(i)
  
  sublists = [ lst[0 : cuts[0]] ]
  for c in range(1, len(cuts)):
    sublists.append( lst[ cuts[c-1]+1 : cuts[c] ] )
  sublists.append( lst[ cuts[-1]+1 : ] )
  return sublists   
​
def numbers_to_ranges(lst):
  if lst == []:
    return lst
  divided = [ sorted(lst)[0] ]
  for i in range(1,len(lst)):
    if sorted(lst)[i] == sorted(lst)[i-1] + 1:
      divided.append( sorted(lst)[i] )
    else:
      divided.append( 'x' )
      divided.append( sorted(lst)[i] )
  divided = divide_list(divided, 'x')
  
  output = []
  for sublist in divided:
    if len(sublist) == 1:
      output.append( str(sublist[0]) )
    else:
      output.append( str(sublist[0]) + '-' + str(sublist[-1]) )
  return output

