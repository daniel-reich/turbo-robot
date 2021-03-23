"""


Create a function that turns a list of words into a comma separated list,
where the last word is separated by the word "and".

### Examples

    words_to_sentence(["edabit"]) ➞ "edabit"
    
    words_to_sentence(["Hello", "", "Bye"]) ➞ "Hello and Bye"
    
    words_to_sentence(["Hello", "Bye", "See you soon"]) ➞ "Hello, Bye and See you soon"

### Notes

`None` values, empty lists or lists with only empty or `None` values should
return an empty string: `""`

"""

def words_to_sentence(words):
  cleaned_words  = words and [e for e in words if e != ""];
  if (cleaned_words is None or len(cleaned_words) == 0) :
    return "";
  if (len(cleaned_words) == 1):
    return cleaned_words[0];
    
  left = cleaned_words[0:-1];
  right = cleaned_words[-1];
  return "{0} and {1}".format(", ".join(left) , right);

