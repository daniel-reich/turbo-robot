"""


Write a function that returns the **length of the shortest contiguous
sublist** whose sum of all elements **strictly exceeds** `n`.

### Examples

    min_length([5, 8, 2, -1, 3, 4], 9) ➞ 2
    
    min_length([3, -1, 4, -2, -7, 2], 4) ➞ 3
    # Shortest sublist whose sum exceeds 4 is: [3, -1, 4]
    
    min_length([1, 0, 0, 0, 1], 1) ➞ 5
    
    min_length([0, 1, 1, 0], 2) ➞ -1

### Notes

  * The sublist should be composed of **contiguous elements** from the original list.
  * If no such sublist exists, return `-1`.

"""

def min_length(lst, n):
  successful_lst = []
  for num in range(len(lst)):
    print('>>>>>'+str(num))
    sum = 0
    num_nums = 0
    for i in range(num, len(lst)):
      if sum > n:
        print('appended', num_nums)
        successful_lst.append(num_nums)
        break
      sum += lst[i]
      print('here?')
      num_nums +=1
      if sum > n:
        print('appended', num_nums)
        successful_lst.append(num_nums)
        break
  print(successful_lst)
  if successful_lst == []:
    return -1
  smallest = successful_lst[0]
  for num in successful_lst:
    if smallest > num:
      smallest = num
  return smallest

