"""


Given a string of digits, return the longest substring with _alternating_
odd/even or even/odd digits. If two or more substrings have the same length,
return the substring that occurs first.

### Examples

    longest_substring("225424272163254474441338664823") ➞ "272163254"
    # substrings = 254, 272163254, 474, 41, 38, 23
    
    longest_substring("594127169973391692147228678476") ➞ "16921472"
    # substrings = 94127, 169, 16921472, 678, 476
    
    longest_substring("721449827599186159274227324466") ➞ "7214"
    # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
    # 7214 and 9274 have same length, but 7214 occurs first.

### Notes

The minimum alternating substring size is 2.

"""

def longest_substring(digits):
    lst = []
    ind = []
    count = 0
    binary = [1 if i else 0 for i in [int(i) % 2 == 0 for i in digits]]
    for i in range(len(binary) - 1):
        if binary[i + 1] - binary[i] != 0:
            count += 1
            if i == 28:
                ind.append(i)
                lst.append(count)
        else:
            ind.append(i)
            lst.append(count)
            count = 0
    lst = [i + 1 for i in lst]
    ind = [i + 1 for i in ind]
​
    length_index = lst.index(max(lst))
​
    if length_index == 0:
        starting_index = 0
    else:
        starting_index = ind[length_index - 1]
​
    return digits[starting_index : max(lst) + starting_index]

