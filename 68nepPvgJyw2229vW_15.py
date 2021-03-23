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

def pairwise_swap(list_of_elements):
  if len(list_of_elements) % 2 == 0:
    swapped_list = []
    for i in range(0, len(list_of_elements), 2):
      swapped_list += list(reversed(list_of_elements[i:i+2]))
    return swapped_list
  else:
    if len(list_of_elements) == 1:
      return list_of_elements
    last_element = list_of_elements[-1]
    list_of_elements = pairwise_swap(list_of_elements[:-1])
    ord_list = [list(str(i)) for i in list_of_elements]
    ord_list = [sum([ord(j) for j in i]) for i in ord_list]
    ascii_max_location = 0
    for i in range(1, len(ord_list)):
      if ord_list[i] > ord_list[ascii_max_location]:
        ascii_max_location = i
    if ord_list[ascii_max_location] > sum([ord(i) for i in list(str(last_element))]):
      list_of_elements.append(list_of_elements[ascii_max_location])
      list_of_elements[ascii_max_location] = last_element
    else:
      list_of_elements.append(last_element)
    return list_of_elements

