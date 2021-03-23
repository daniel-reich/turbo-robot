"""


For a given list, determine the biggest possible sum between consecutive
terms, as well as the initial and final position of the terms.

### Examples

    big_sub([4, -3, 5, -7, 5]) ➞ [6 (sum), 0 (start), 2 (end)]
    
    big_sub([4, -3, -5, 7, 5]) ➞ [12, 3, 4]
    
    big_sub([2, -3, 2, -3, 2]) ➞ [2, 4, 4]

### Notes

  * If the biggest sum is repeated at several intervals, return the starting and ending positions of the latest interval.
  * The list will always have positive numbers.

"""

def big_sub(lst):
    best_sum, current_sum = lst[0] , lst[0]
    start = [0]
    end = 0
    for i in range(1,len(lst)):
        if len(start) > 4:
            start = [0] 
        current_sum = max(lst[i],current_sum + lst[i])
        if current_sum >= best_sum:
            best_sum = current_sum
            end = i
        if current_sum <= 0:
            start.append(i + 1)
    return [best_sum,start[-1] if start[-1] <= end else start[-2],end]

