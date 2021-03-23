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
    l1 = [ x for x in lst if x == str(x)]
    l2 = [x for x in lst if x!=str(x)]
    l1.sort(),l2.sort()
    ls=[]
    for i,j in zip(l1,l2):
        ls.append(j),ls.append(i)
    return ls
print(alternate_sort(["a", "b", "c", 1, 2, 3]))

