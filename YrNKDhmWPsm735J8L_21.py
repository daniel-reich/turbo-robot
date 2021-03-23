"""


A student learning Python was trying to make a function that sorts all the
letters of a word, but their code is broken, and they can't figure out why.

Spot and fix the error(s) in the code to make the function work. As an added
challenge for those who are more advanced, see if you can shrink (the fixed
version of) the student's code down to only a single line.

### Examples

    sort_word("dcba") ➞ "abcd"
    
    sort_word("Unpredictable") ➞ "Uabcdeeilnprt"
    # Capital letters should come first.
    
    sort_word("pneumonoultramicroscopicsilicovolcanoconiosis") ➞ "aacccccceiiiiiilllmmnnnnooooooooopprrsssstuuv"

### Notes

If you're trying to get a function definition into a single line, try
assigning a variable to a lambda function.

"""

#One line? This is close enough.
def sort_word(word):
    result1 = []
    result2 = []
    result3 = ''
    for i in word:
        if i.isupper():
            result1 += i
        elif i.islower():
            result2 += i
        else:
            result3 += i
    result1.sort()
    result2.sort()
    result1.extend(result2)
    for i in result1:
        result3 += i
    return result3

