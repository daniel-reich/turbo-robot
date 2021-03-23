"""


Create a function to **bridge shuffle** two lists. To **bridge shuffle** , you
interleave the elements from both lists in an alternating fashion, like so:

    List 1 = ["A", "A", "A"]
    List 2 = ["B", "B", "B"]
    
    Shuffled List = ["A", "B", "A", "B", "A", "B"]

This can still work with two lists of uneven length. We simply tack on the
extra elements from the longer list, like so:

    List 1 = ["C", "C", "C", "C"]
    List 2 = ["D"]
    
    Shuffled List = ["C", "D", "C", "C", "C"]

Create a function that takes in two lists and returns the bridge-shuffled
list.

### Examples

    bridge_shuffle(["A", "A", "A"], ["B", "B", "B"]) ➞ ["A", "B", "A", "B", "A", "B"]
    
    bridge_shuffle(["C", "C", "C", "C"], ["D"]) ➞ ["C", "D", "C", "C", "C"]
    
    bridge_shuffle([1, 3, 5, 7], [2, 4, 6]) ➞ [1, 2, 3, 4, 5, 6, 7]

### Notes

  * Elements in both lists can be strings or integers.
  * If two lists are of unequal length, add the additional elements of the longer list to the end of the shuffled list.
  * Always start your shuffle with the first element of List 1.

"""

def bridge_shuffle(lst1, lst2):
    if not lst1 and not lst2:
        return []
    elif not lst1:
        return lst2
    elif not lst2:
        return lst1
    result = [lst1[0], lst2[0]]
    for i in range(1, min(len(lst1), len(lst2))):
        result.append(lst1[i])
        result.append(lst2[i])
    if len(lst1) > len(lst2):
        result.extend(lst1[len(lst2):])
    else:
        result.extend(lst2[len(lst1):])
    return result

