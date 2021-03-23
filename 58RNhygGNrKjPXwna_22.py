"""


Write a function that returns the **longest non-repeating substring** for a
string input.

### Examples

    longest_nonrepeating_substring("abcabcbb") ➞ "abc"
    
    longest_nonrepeating_substring("aaaaaa") ➞ "a"
    
    longest_nonrepeating_substring("abcde") ➞ "abcde"
    
    longest_nonrepeating_substring("abcda") ➞ "abcd"

### Notes

  * If multiple substrings tie in length, return the one which occurs **first**.
  *  **Bonus** : Can you solve this problem in **linear time**?

"""

def longest_nonrepeating_substring(txt):
  current_sub_string = ''
  whole_sub_strings = ''
  letters_and_index = {}
  length = len(txt)
  indexes = 0
  while indexes != length:
    letter = txt[indexes]
    print(letter)
    if letter not in current_sub_string:
      current_sub_string += letter
      letters_and_index[letter] = indexes
      indexes += 1
      print(current_sub_string)
    else:
      if len(current_sub_string) > len(whole_sub_strings):
        whole_sub_strings = current_sub_string
​
      current_sub_string = ''
      indexes = letters_and_index[letter] + 1
      letters_and_index = {}
  if len(current_sub_string) > len(whole_sub_strings):
    whole_sub_strings = current_sub_string
  return whole_sub_strings
​
# 1- start at the beging - i_am_a_string
# 2- keep going left intill there is a repeat - i_am_
# 3- make this sublist a verariable
# 4-find were the repeat ocurs in the string - a
# 5-start agin in fron of repeat - m_a_string
# 6- when steep 3 if sublist is smaller leave the other sublist the same
# 7-repeat intil the end of the string

