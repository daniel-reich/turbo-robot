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
    digits=digits+digits[-1]
    lst=list(map(int,digits))
    lst1=list(lst)
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i]='E'
        else:
            lst[i]='O'
    j=0
    substrings=[]
    while True:
        if j==len(lst):
            break
        last=lst[j]
        for k in range(j,len(lst)):
            if lst[k]!=last:
                last=lst[k]
            else:
                substrings.append(''.join(str(e) for e in lst1[j-1:k]))
                j=k+1
                continue
    maxstr=1
    sub=None
    for i in substrings:
        if len(i)>maxstr:
            maxstr=len(i)
            sub=i
    return sub

