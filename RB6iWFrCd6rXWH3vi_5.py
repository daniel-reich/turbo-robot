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

odd = {str(x) for x in (1,3,5,7,9)}
even = {str(x) for x in (0,2,4,6,8)}
​
def longest_substring(s):
    assert len(s) > 0
    curr_seq = s[0]
    last_odd = s[0] in odd
    longest_seq = ''
    for c in s[1:]:
        if (c in odd) != last_odd:
            curr_seq += c
        else:
            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
            curr_seq = c
        last_odd = c in odd
    if len(curr_seq) > len(longest_seq):
        longest_seq = curr_seq
​
    return longest_seq

