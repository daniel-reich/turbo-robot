"""


A long stretch of beach is represented by a string of two characters `0` \-
free, `1` \- occupied. Due to recent restrictions, a new person cannot take
place next to another. There has to be one free place between two people
lounging on the beach. Create a function to compute how many new people at
most can settle in on the given beach.

### Examples

    sun_loungers("10001") ➞ 1
    # Can take place in the middle.
    
    sun_loungers("00101") ➞ 1
    # Can take place on the left.
    
    sun_loungers("0") ➞ 1
    # Can take one place.
    
    sun_loungers("000") ➞ 2
    # Can take places on the left and on the right.

### Notes

N/A

"""

def sun_loungers(beach):
    result = 0
    beach = list(beach)
    for i in range(len(beach)):
        prev = beach[i-1:i]
        next = beach[i+1:i+2]
        if beach[i] == '0':
            if prev != ['1'] and next != ['1']:
                beach[i] = '1'
                result += 1
    return(result)

