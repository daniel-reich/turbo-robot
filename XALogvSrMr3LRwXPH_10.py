"""


Given a list of _10 numbers_ , return whether or not the list is shuffled
sufficiently enough. In this case, if **3 or more** numbers appear
**consecutively** (ascending or descending), return `False`.

### Examples

    is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
    # 1, 2, 3 appear consecutively
    
    is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
    # 9, 8, 7, 6 appear consecutively
    
    is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
    # No consecutive numbers appear
    
    is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
    # No consecutive numbers appear

### Notes

  * Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
  * You will get numbers from 1-10.

"""

def is_shuffled_well(lst):
    l=[]
    new_l_posi=[]
    new_l_neg=[]
    for i,j in zip(lst,lst[1:]):
        t=i-j
        l.append(t)
​
    if l.count(-1) >= 2 or l.count(1) >= 2:
        for each in range(0,len(l)):
            if l[each]==1:
                new_l_posi.append(each)
            elif l[each]==-1:
                new_l_neg.append(each)
        for posi,num_1 in zip(new_l_posi,new_l_posi[1:]):
            if posi-num_1==-1:
                return False
​
        for neg,num_2 in zip(new_l_neg,new_l_neg[1:]):
            if neg - num_2 == -1:
                return False
​
​
    return True

