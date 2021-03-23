"""


Given two words, the **letter distance** is calculated by taking the absolute
value of the difference in character codes and summing up the difference.

If one word is longer than another, add the difference in lengths towards the
score.

To illustrate:

    letter_distance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.length, fly.length)
    
    = |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
    = 2 + 3 + 4 + 2
    = 11

### Examples

    letter_distance("sharp", "sharq") ➞ 1
    
    letter_distance("abcde", "Abcde") ➞ 32
    
    letter_distance("abcde", "bcdef") ➞ 5

### Notes

  * Always start comparing the two strings from their first letter.
  * Excess letters are not counted towards distance.
  * Capital letters are included.

"""

def letter_distance(txt1,txt2):
    final_array = []
    sum = 0
    list_1 = list(txt1)
    list_2 = list(txt2)
    if len(list_1) > len(list_2):
        for i in range(len(list_2)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
        d = len(list_1) - len(list_2)
        final_array.append(abs(d))
    elif len(list_1) == len(list_2):
        for i in range(len(list_2)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
    else:
        for i in range(len(list_1)):
            a = ord(list_1[i])
            b = ord(list_2[i])
            c = a - b
            final_array.append(abs(c))
        d = len(list_2) - len(list_1)
        final_array.append(abs(d))
    for i in range(len(final_array)):
        sum = sum + final_array[i]
    return sum

