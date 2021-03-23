"""


The _mode_ of a group of numbers is the value (or values) that occur most
often (values have to occur more than once). Given a sorted list of numbers,
return a list of all modes in ascending order.

### Examples

    mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 
    
    mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]
    
    mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6] 

### Notes

In this challenge, all group of numbers will have at least one mode.

"""

def mode(nums):
 # create set --> unique elements
 nums_set=set(nums)
 #print(nums_set)
 count_dict={}
 # go through unique elements
 for element in nums_set:
  # count occurences
  count=0
  for i in range(0,len(nums)):
   if nums[i] == element:
    count+=1
  # update dictionary
  count_dict.update({element:count})
 #print(count_dict)
 # determine highest counts
 highest=1
 for c in count_dict.values():
  if c > highest:
   highest=c
 #print(highest)
 # create list with nums that have the highest count
 output=[]
 for keys in count_dict.keys():
  if count_dict[keys] == highest:
   output.append(keys)
 return sorted(output)

