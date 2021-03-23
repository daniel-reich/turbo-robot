"""


Given a string of letters, create a function that returns a list with the
separator that yields the longest possible substring, provided that:

  * The substring starts and ends with the separator.
  * The separator doesn't occur inside the substring other than at the ends.

If two or more separators yield substrings with the same length, they should
appear in alphabetical order.

### Examples

    max_separator("supercalifragilistic") ➞ ["s"]
    # The longest substring is "supercalifragilis".
    
    max_separator("laboratory") ➞ ["a", "o", "r"]
    # "abora", "orato" and "rator" are the same length.
    
    max_separator("candle") ➞ []
    # No possible substrings.

### Notes

  * All substrings should be at least of length 2 (i.e. no single-letter substrings).
  * Expect lowercase alphabetic characters only.

"""

def max_separator(str):
    max_width = 0
    best_letter = dict()
    for position in range(len(str)):
        
        length = 0
        current = str[position]
        
        for letter in str[position + 1:]:
            length += 1
            if letter == current:
                if (length >= max_width):
                    
                    best_letter[current] = length;
                    
                    max_width = length
                    break
                else:
                    break
​
            
    longest_substring_letters = []
    for i in best_letter:
        if best_letter[i] == max_width:
            longest_substring_letters.append(i)
        
    return sorted(longest_substring_letters)

