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
    count = 0
    beach2 = '0'
    for i,j in enumerate(beach):
        foll = beach[i + 1] if i + 1 < len(beach) else '0' 
        prev = beach2[i]
        if j == '0':
            if prev == '0' and foll == '0':
                count += 1
                beach2 += '1'
            else:
                beach2 += j        
        else:
            beach2 += j
    return count

