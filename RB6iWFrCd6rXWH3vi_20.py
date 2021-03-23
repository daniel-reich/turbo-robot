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

def longest_substring(input):
    sublst=[]
    outputlst=[]
    output=[]
    result=''
    input=list(input)
    length=0
​
​
    for n in range(1, len(input)):
        if n==len(input)-1:
            if int(input[n-1])%2 != int(input[n])%2:
                sublst.append(input[n-1])
                sublst.append(input[n])
                outputlst.append(sublst)
                break
        if int(input[n])%2 != int(input[n-1])%2:
            sublst.append(input[n-1])
        else:
            sublst.append(input[n-1])
            if len(sublst)>1: outputlst.append(sublst)
            sublst=[]
​
​
    for item in outputlst:
        length=max(length,len(item))
​
​
    for item in outputlst:
        if len(item)==length:
            output=item
            break
​
​
    for item in output:
        result=result+str(item)
    print(result)
​
    return(result)

