"""


Create a function that takes a list of numbers. Return the largest number in
the list.

### Examples

    findLargestNum([4, 5, 1, 3]) ➞ 5
    
    findLargestNum([300, 200, 600, 150]) ➞ 600
    
    findLargestNum([1000, 1001, 857, 1]) ➞ 1001

### Notes

  * Expect either positive numbers or zero (there are no negative numbers).
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def findLargestNum(nums):
    largest, left, right = nums[0], 1, len(nums)-1
    while left<=right:
        if nums[left]>largest:
            largest = nums[left]
        if nums[right]>largest:
            largest = nums[right]
        left += 1
        right -= 1
    return largest

