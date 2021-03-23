"""


Given an element in a list, write a function to determine the length of a
particular element's **sorting cycle**. Given one element in the list, a
**sorting cycle** is the number of swaps it takes so that the last displaced
swapped item is back in its correct order.

What is the length of 9's **sorting cycle**?

    [1, 9, 8, 4, 7, 2, 6, 3, 5]
    [1, 5, 8, 4, 7, 2, 6, 3, 9]  # 9 swaps with 5; 9 is in its correct spot.
    [1, 7, 8, 4, 5, 2, 6, 3, 9]  # 5 replaces 7; 5 is in its correct spot.
    [1, 6, 8, 4, 5, 2, 7, 3, 9]  # 7 replaces 6; 7 is in its correct spot.
    [1, 2, 8, 4, 5, 6, 7, 3, 9]  # 6 replaces 2; 6 is in its correct spot and 2 is in it's correct spot - done!

9's cycle is of length **4**. Notice how every number included in the swap (9,
5, 7, 6, and 2) are all in their rightful places. This is because each of
these numbers are in the same sorting cycle.

Here is another example. Using the same list above, what is the length of 8's
**sorting cycle**?

    [1, 9, 8, 4, 7, 2, 6, 3, 5]
    [1, 9, 3, 4, 7, 2, 6, 8, 5] # 8 replaces 3; 8 and 3 are both in their correct spots.

8's cycle is of length **1**.

### Examples

    cycle_length([1, 5, 4, 3, 2, 6], 4) ➞ 1
    
    cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 7) ➞ 7
    
    cycle_length([43, 81, 88, 93, 17, 32, 19, 11], 93) ➞ 5
    
    cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 1) ➞ 0

### Notes

  * Output `0` if the element is already in its correct order (see example #4).
  * If this question is confusing, think about it in this way:
    * Normally, swapping two numbers to place the first number in the correct order does not place the second number in its correct order. In other words, it's a single-party beneficial sort.
    * The sorting cycle ends when a swap leads to a mutually beneficial sort, e.g. swapping two numbers leads the first AND the second number to be put to their rightful places.
  * This question is tricky — see the **Comments** for a hint if you're stuck.

"""

def simplify_problem(lst, n):
    s_list = [lst.index(i) for i in sorted(lst)]
    s_n = s_list[lst.index(n)]
    return s_list, s_n
​
​
def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst
​
​
def find_and_swap(lst, n, count=1):
    # lst = [0, 2, 3, 1, 4]
    # n = 2
    print('Problem: {}'.format((lst, n)))
    origin_index = lst.index(n)
    target_index = n
    print('Origin: {}  ' 'Target: {}'.format(origin_index, target_index))
​
    if origin_index == target_index:
        print('Origin == Target --> break')
        count = 0
​
    lst = swap(lst, origin_index, target_index)
    # lst.insert(target_index, lst.pop(origin_index))
    print('Swapped: {}'.format((lst, lst[origin_index])))
    return lst, lst[origin_index], count
​
​
def cycle_length(lst, n):
    simple_list, simple_n = simplify_problem(lst, n)
    counter = 0
    while True:
        simple_list, simple_n, count = find_and_swap(simple_list.copy(), simple_n)
        if count:
            counter += 1
        else:
            break
    return counter

