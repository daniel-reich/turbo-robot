"""


Given a string `s`, return the length of the longest palindrome that can be
built with those letters.

### Examples

    longest_palindrome("a") ➞ 1
    
    longest_palindrome("bb") ➞ 2
    
    longest_palindrome("abccccdd") ➞ 7
    
    longest_palindrome("") ➞ 0

### Notes

N/A

"""

def longest_palindrome(s):
  rem_and_count_even_occ = lambda str: [[l8r for l8r in s if s.count(l8r) % 2 == 1], len(s) - len([l8r for l8r in s if s.count(l8r) % 2 == 1])] 
  odd_sorter = lambda list: {l8r: list.count(l8r) for l8r in set(list)}
  
  def odd_counter(dict):
    used = False
    count = 0
    
    for key in dict.keys():
      if dict[key] == max(dict.values()) and used == False:
        count += dict[key]
        used = True
      else:
        count += dict[key] - 1
    
    return count
  
  raceo = rem_and_count_even_occ(s)
  os = odd_sorter(raceo[0])
  
  return raceo[1] + odd_counter(os)

