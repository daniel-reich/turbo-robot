"""


To train for an upcoming marathon, Johnny goes on one long-distance run each
Saturday. He wants to track how often the number of miles he runs exceeds the
**previous** Saturday. This is called a **progress day**.

Create a function that takes in a list of miles run every Saturday and returns
Johnny's total number of progress days.

### Examples

    progress_days([3, 4, 1, 2]) ➞ 2
    # There are two progress days, (3->4) and (1->2)
    
    progress_days([10, 11, 12, 9, 10]) ➞ 3
    
    progress_days([6, 5, 4, 3, 2, 9]) ➞ 1
    
    progress_days([9, 9])  ➞ 0

### Notes

Running the **same number of miles** as last week does not count as a progress
day.

"""

def progress_days(runs):
  i = 1
  count = 0
  while(i<len(runs)):
    if runs[i] > runs[i-1]:
      count +=1
    i+=1
  return count

