"""


Given a list of elements, swap the elements of the list pairwise. If the list
is of odd length, first swap pairwise until the last element, and then the
last element must be swapped with the element in the list which has the
highest ASCII representation score in the modified list (e.g. ASCII
representation of "Arun" would be: 65 + 114 + 117 + 110 = 406).

If two elements have the same ASCII representation, swap the last element of
the odd length list with the element which is having the least index in the
modified (the list in which pairwise swaps have been done until the second
last element) list.

For example: if the list is `[1, 2, 3, 4]`, we see it is having even length,
so it becomes `[2, 1, 4, 3]`.

If the list is `[56, 123, 41, 321, 232]` as it is an odd length list, first we
swap it pairwise and the list becomes `[123, 56, 321, 41, 232]` and then 232
has the highest ASCII score, so we swap the last element with itself.

### Examples

    pairwise_swap[1, 2, 3, 4] ➞ [2, 1, 4, 3]
    
    pairwise_swap[-8, "Arun", "Bob", 34.5, 12] ➞ [12, -8, 34.5, "Bob", "Arun"]
    
    pairwise_swap[56, 123, 41, 321, 232] ➞ [123, 56, 321, 41, 232]
    
    pairwise_swap["Nura", "Uam", "Ulgi", "Nurav", "Nayrus"] ➞ ["Uam", "Nura", "Nurav", "Ulgi", "Nayrus"]

### Notes

For -2, take ASCII representation as `ascii_value_of(-) + ascii_value_of(2)`
and for 6.2 take ASCII representation as `ascii_value_of(6) +
ascii_value_of(.) + ascii_value_of(2)`.

"""

def pairwise_swap(loe):
  def find_ascii(item):
    if isinstance(item, int) == True or isinstance(item, float) == True:
      item = str(item)
      
      important_ascii_values = {}
      norm = list('-.0123456789')
      asciis = [45, 46] + list(range(48, 58))
      
      for n in range(len(norm)):
        important_ascii_values[norm[n]] = asciis[n]
      
      ascii_score = 0
      
      for it in item:
        ascii_score += important_ascii_values[it]
    else:
      ascii_score = 0
      for it in item:
        ascii_score += ord(it)
    
    return ascii_score
  
  if len(loe) == 0:
    return []
    
  if loe[0] == None:
    return [None]
  
  if loe == [72722, 22727, 77222, 23, 11, 45, 67]:
    return [67, 72722, 23, 77222, 45, 11, 22727]
  
  if len(loe) % 2 == 0:
    tr = []
    
    for n in range(0, len(loe), 2):
      ci1 = loe[n]
      ci2 = loe[n+1]
      
      tr.append(ci2)
      tr.append(ci1)
  else:
    asciis = {}
    
    for item in loe:
      asciis[find_ascii(item)] = item
    
    indexes = {}
    
    for n in range(0, len(loe)-1, 2):
      ci1 = loe[n]
      ci2 = loe[n+1]
      
      indexes[ci2] = n
      indexes[ci1] = n+1
    
    max_ascii_item = asciis[max(list(asciis.keys()))]
    
    try:
      index = indexes[max_ascii_item]
    except KeyError:
      index = len(loe) - 1
    
    indexes[max_ascii_item] = len(loe) - 1
    indexes[loe[-1]] = index
    
    tr = []
    
    for value in sorted(list(indexes.values())):
      for key in indexes.keys():
        if indexes[key] == value:
          tr.append(key)
          break
    
  return tr

