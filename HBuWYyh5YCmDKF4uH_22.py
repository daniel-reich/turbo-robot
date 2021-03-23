"""


An **almost-sorted sequence** is a sequence that is **strictly increasing** or
**strictly decreasing** if you remove a **single element** from the list (no
more, no less). Write a function that returns `True` if a list is **almost-
sorted** , and `False` otherwise.

For example, if you remove `80` from the first example, it is perfectly sorted
in ascending order. Similarly, if you remove `7` from the second example, it
is perfectly sorted in descending order.

### Examples

    almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True
    
    almost_sorted([6, 5, 4, 7, 3]) ➞ True
    
    almost_sorted([6, 4, 2, 0]) ➞ False
    // Sequence is already sorted.
    
    almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
    // Requires removal of more than 1 item.

### Notes

  * Completely sorted lists should return `False`.
  * Lists will always be **> 3** in length (to remove ambiguity).
  * Numbers in each input list will be unique - don't worry about "ties".

"""

def almost_sorted(lst) :
    def chk_if_sorded(chk_lst):
        lst_chk = [(chk_lst[x] < chk_lst[x + 1]) for x in range(len(chk_lst) - 1)]
        if all(lst_chk) or not any(lst_chk) : return True
        return False
    if not chk_if_sorded(lst):
        for indx in range(len(lst)):
            n_lsr = lst.copy()
            n_lsr.pop(indx)
            if chk_if_sorded(n_lsr): return True
        return False
    else:return False

