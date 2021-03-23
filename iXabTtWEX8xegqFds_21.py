"""


Write a function that sorts a given list in an aletrnative fashion. The result
should be a list sorted in ascending order (number then letter). Lists will
contain equal amounts of integer numbers and single characters.

### Examples

    alternate_sort(["a", "b", "c", 1, 2, 3]) ➞ [1, "a", 2, "b", 3, "c"]
    
    alternate_sort([-2, "f", "A", 0, 100, "z"]) ➞ [-2, "A", 0, "f", 100, "z"]
    
    alternate_sort(["X", 15, 12, 18, "Y", "Z"]) ➞ [12, "X", 15, "Y", 18, "Z"]

### Notes

N/A

"""

def alternate_sort(lst):
  a,n = sorted(i for i in lst if type(i)==str),sorted(i for i in lst if type(i)==int)
  return sum([[j,i] for i,j in zip(a,n)],[])

