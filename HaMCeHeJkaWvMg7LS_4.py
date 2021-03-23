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
    
    beach = [x for x in beach]
    
    chairs = 0
    i = 0
    while i < len(beach):
        if beach[i] == '0':
            if i == 0:
                try:
                    if beach[i+1] == '0':
                        chairs += 1
                        beach[i] = '1'
                        i += 1
                    else:
                        i += 1
                except: 
                    chairs += 1
                    i += 1
                
            elif i == len(beach) - 1:
                if beach[i - 1] == '0':
                    chairs += 1
                    i += 1
                else:
                    i += 1
            else:
                if beach[i-1] == '0' and beach[i+1] == '0':
                    chairs += 1
                    beach[i] = '1'
                    i += 1
​
                else:
                    i += 1
        else: 
            i += 1
    return chairs

