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
    beach_list = list(beach)
    if len(beach) == 1:
        if beach_list[0] == 1:
            return 0
        return 1
    for index, character in enumerate(beach_list):
        if character == '1':
            continue
        if index == 0:
            if beach_list[index + 1] == '0':
                count += 1
                beach_list[index] = '1'
        elif index == len(beach_list) - 1:
            if character == '0':
                if beach_list[index - 1] == '0':
                    count += 1
        elif beach_list[index - 1] == '0' and beach_list[index + 1] == '0':
            count += 1
            beach_list[index] = '1'
​
    return count

