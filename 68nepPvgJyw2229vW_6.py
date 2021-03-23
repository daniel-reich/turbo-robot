"""


Given a list of elements, swap the elements of the list pairwise. If the list
is of odd length, first swap pairwise until the last element, and then the
last element must be swapped with the element in the list which has the
highest ASCII representation score in the modified list (e.g. ASCII
representation of "Arun" would be: 65 + 114 + 117 + 110 = 406).

If two elements have the same ASCII representation, swap the last element of
the odd length list with the element which is having the least index in the
modified (the list in which pairwise swaps have been done until the second
last element) list.

For example: if the list is `[1, 2, 3, 4]`, we see it is having even length,
so it becomes `[2, 1, 4, 3]`.

If the list is `[56, 123, 41, 321, 232]` as it is an odd length list, first we
swap it pairwise and the list becomes `[123, 56, 321, 41, 232]` and then 232
has the highest ASCII score, so we swap the last element with itself.

### Examples

    pairwise_swap[1, 2, 3, 4] ➞ [2, 1, 4, 3]
    
    pairwise_swap[-8, "Arun", "Bob", 34.5, 12] ➞ [12, -8, 34.5, "Bob", "Arun"]
    
    pairwise_swap[56, 123, 41, 321, 232] ➞ [123, 56, 321, 41, 232]
    
    pairwise_swap["Nura", "Uam", "Ulgi", "Nurav", "Nayrus"] ➞ ["Uam", "Nura", "Nurav", "Ulgi", "Nayrus"]

### Notes

For -2, take ASCII representation as `ascii_value_of(-) + ascii_value_of(2)`
and for 6.2 take ASCII representation as `ascii_value_of(6) +
ascii_value_of(.) + ascii_value_of(2)`.

"""

def pairwise_swap(list_of_elements):
    odd = True
    newlst, a, top, val  = [], len(list_of_elements), 0, 0
    if a % 2 == 0: 
        for i in range(a):
            if odd:
                newlst += [list_of_elements[i+1]]
                odd = False
                continue
            else:
                newlst += [list_of_elements[i-1]]
                odd = True
        return newlst
    for i in range(a):
        if len(newlst) == len(list_of_elements) - 1:
            break
        if odd:
            newlst += [list_of_elements[i+1]]
            odd = False
            continue
        else:
            newlst += [list_of_elements[i-1]]
            odd = True   
    newlst.append(list_of_elements[-1])
    high = newlst[0]
    for i in str(newlst[0]):
        top += ord(i)
    for i in list_of_elements:
        for x in str(i):
            val += ord(x)
        if val == top:
            if newlst.count(high) > newlst.count(i):
                high = i
                continue
        if val > top:
            top = val
            high = i
        val = 0
    newlst[newlst.index(high)], newlst[-1] = newlst[-1], newlst[newlst.index(high)]
    return newlst

