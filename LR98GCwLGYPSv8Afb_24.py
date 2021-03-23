"""


Given a list of words in the singular form, return a set of those words _in
the plural form_ **if they appear more than once in the list.**

###  Examples

    pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
    
    pluralize(["table", "table", "table"]) ➞ { "tables" }
    
    pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

### Notes

  * This is an **oversimplification** of the English language so no edge cases will appear.
  * Only focus on whether or not to add an **s** to the ends of words.
  * All tests will be valid.

"""

def pluralize(list):
  
  # Local variables 
  plural_words = set()
  words_count = 0
  
  # Loop through the list 
  for word in list:
    # Get the number of times word appears in list 
    words_count = list.count(word)
    
    # Check if word count is greater then one, and doesn't belong in set
    if words_count > 1 and word + "s" not in plural_words:
      # Add an 's' at the end of the word 
      word += 's'
      
      # Store the word inside a set 
      plural_words.add(word)
    
    elif word + 's' not in plural_words:
      # Store the word, without an 's', in set 
      plural_words.add(word)
  
  # Return the set 
  return plural_words

