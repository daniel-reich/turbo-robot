"""


Mona has created a method to sort a list in ascending order.

Starting from the left of the list, she compares numbers by pairs. If the
first pair is ordered `[smaller number, larger number]`, she moves on. If the
first pair is ordered `[larger number, smaller number]`, she swaps the two
integers before moving on to the next pair. She repeats this process until she
reaches the end of the list.

Then, she moves back to the beginning of the list and repeats this process
until the entire list is sorted.

If the unsorted list is: `[3, 9, 7, 4]`, she will perform the following steps
(note _Swaps_ here refers to cumulative swaps):

  1. She starts with the first pair.
  2. `[3, 9]` is in order, move on. List: `[3, 9, 7, 4]`. Swaps: `0`.
  3. `[9, 7]` is not. Swap. List: `[3, 7, 9, 4]`. Swaps: `1`
  4. `[9, 4]` is not. Swap. List: `[3, 7, 4, 9]`. Swaps: `2`
  5. Check if list is sorted. It is not, so start over at first pair.
  6. `[3, 7]` is in order, move on. List: `[3, 7, 4, 9]`. Swaps: `2`
  7. `[7, 4]` is not. Swap. List: `[3, 4, 7, 9]`. Swaps: `3`.
  8. `[7, 9]` is in order, move on. List: `[3, 4, 7, 9]`. Swaps: `3`.
  9. Check if list is sorted. It is. End.

Sorting the list `[3, 9, 7, 4]` takes her _3 swaps_. Write a function that
takes in an unsorted list and returns the number of swaps it takes for the
list to be sorted according to Mona's algorithm.

### Examples

    number_of_swaps([5, 4, 3]) ➞ 3
    
    number_of_swaps([1, 3, 4, 5]) ➞ 0
    
    number_of_swaps([5, 4, 3, 2]) ➞ 6

### Notes

N/A

"""

def number_of_swaps(lst):
  count = 0
  while lst != sorted(lst):
    for i in range(len(lst) - 1):
      if lst[i] <= lst[i+1]:
        continue
      else:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        count += 1
  return count

