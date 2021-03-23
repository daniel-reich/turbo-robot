"""


Create a function that takes a string containing both name and number of
animals and plants that may or may not be found in Chitwan National Park. The
function should return a list of tuples where first element in the tuple is
animal name and second element in the tuple is number of that particular
animal that is found in Chitwan National Park.

### Animals Present in Chitwan National Park

    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

### Examples

    fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
    # Mango not present in animal list.
    
    fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
    # Apples not present in animal list.

### Notes

  * Input contains name and number of both animals and plants.
  * If there is no match, return an empty list.

"""

def fauna_number (txt):
  other_words  = ['There','are','and']
  animals_list = []
  number_list  = []
  animals      = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
  word_str     = ''
  word         = []
  ans          = []
  valid_index  = []
  
  for i in txt:
    while i!= '.' and i!=' ' and i!= ',':
      word.append (i)
​
      break
    
    if i == '.' or i == ',' or i == ' ':
      for b in word:
        word_str+= b
​
      try:
          int (word_str)
          number_list.append (word_str)
​
      except:
          if word_str not in other_words:
            animals_list.append (word_str)
​
      word  = []
      word_str = ''
​
   
  for i in range (len (animals_list)):
    if animals_list[i] in animals:
      valid_index.append (i) 
  for c in valid_index:
    tup = (animals_list[c],number_list[c])
​
    ans.append (tup) 
  return ans

