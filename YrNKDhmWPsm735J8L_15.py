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

def sort_word(word):
  list1 = []
  list1[:0]= word
  list1 = sorted(list1)
  final_word = "".join(list1)
  
  return final_word

