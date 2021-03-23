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
  final_word = ""
  uppercase_string = ""
  lowercase_string = ""
  for i in word.split():
    if i == i.upper():
      uppercase_string += i
    else:
      lowercase_string += i
  for i in sorted(uppercase_string):
    final_word += i
  for i in sorted(lowercase_string):
    final_word += i
  return final_word

