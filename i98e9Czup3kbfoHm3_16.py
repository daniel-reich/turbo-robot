"""


Create a function that takes a string as an argument. The function must return
a string containing 1s and 0s based on the string argument's words. If any
word in the argument is not equal to "zero" or "one" (case insensitive), you
should ignore it. The returned string's length should be a multiple of 8, if
the string is not a multiple of 8 you should remove the numbers in excess.

### Examples

    text_to_number_binary("zero one zero one zero one zero one") ➞ "01010101"
    
    text_to_number_binary("Zero one zero ONE zero one zero one") ➞ "01010101"
    
    text_to_number_binary("zero one zero one zero one zero one one two") ➞ "01010101"
    
    text_to_number_binary("zero one zero one zero one zero three") ➞ ""
    
    text_to_number_binary("one one") ➞ ""

### Notes

You must return the result as a string.

"""

def text_to_number_binary(txt):
    conversion_table = {'zero': '0', 'one': '1'}
    # case insensitive, split by space
    words = txt.lower().split(' ')
    # remove unknown words
    words = [w for w in words if w in conversion_table]
    # truncate to multiple of 8
    length = len(words) // 8 * 8
    words = words[:length]
    # translate with the lookup table
    return ''.join(map(conversion_table.get, words))

