"""


In this challenge you will be given a list similar to the following:

    [[3], 4, [2], [5], 1, 6]

In words, elements of the list are _either an integer or a list containing a
single integer_. If you try to sort this list via `sorted([[3], 4, [2], [5],
1, 6])`, Python will whine about not being able to compare integers and lists.

However, us humans can clearly see that this list can reasonably be sorted
according to "the content of the elements" as:

    [1, [2], [3], 4, [5], 6]

Create a function that, given a list similar to the above, sorts the list
according to the "content of the elements".

### Examples

    sort_it([4, 1, 3]) ➞ [1, 3, 4]
    
    sort_it([[4], [1], [3]]) ➞ [[1], [3], [4]]
    
    sort_it([4, [1], 3]) ➞ [[1], 3, 4]
    
    sort_it([[4], 1, [3]]) ➞ [1, [3], [4]]
    
    sort_it([[3], 4, [2], [5], 1, 6]) ➞ [1, [2], [3], 4, [5], 6]

### Notes

To reiterate, elements of the list will be either integers or lists with a
single integer.

"""

def sort_it(lst):
  
  Counter = 0
  Length = len(lst)
  
  Numbers = []
  Lists = []
  Values = []
  
  while (Counter < Length):
    
    Item = lst[Counter]
    Type = type(Item)
    
    if (Type == list):
      Thing = int(Item[0])
      Lists.append(Thing)
      Values.append(Thing)
      Counter += 1
    elif (Type == int):
      Numbers.append(Item)
      Values.append(Item)
      Counter += 1
    else:
      Counter += 1
  
  Values = sorted(Values)
  Answer = []
  
  Counter = 0
  Length = len(Values)
  
  while (Counter < Length):
    
    Item = Values[Counter]
    
    if (Item in Lists):
      Batch = []
      Batch.append(Item)
      Answer.append(Batch)
      Counter += 1
    elif (Item in Numbers):
      Answer.append(Item)
      Counter += 1
    else:
      Counter += 1
    
  return Answer

