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
    n = sorted(list(filter(lambda x:type(x)==int,lst)))[::-1]
    a = sorted(list(filter(lambda x:type(x)!=int,lst)))[::-1]
    res =[]
    for i in range(len(n)):
        res.append(n.pop())
        res.append(a.pop())
    return  res

