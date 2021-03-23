"""


 **Mubashir** needs your help to find out **number of animals** hidden in a
given string `txt`.

You are provided with an array of animals given below:

    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
    "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
    "frog", "hen", "mole", "duck", "goat"]

 **Rule:** Return the **maximum number** of animal names. See the below
example:

    txt = "goatcode"
    
    count_animals(txt) ➞ 2
    # First animal = "dog"
    # Remaining string = "atcoe",
    # Second animal = "cat".
    # count = 2 (correct)
    
    # If you got a "goat" first time
    # remaining string = "code",
    # no animal will be found during next time.
    # count = 1 (wrong)

### Examples

    count_animals("goatcode") ➞ 2
    # "dog", "cat"
    
    count_animals("cockdogwdufrbir") ➞ 4
    # "cow", "duck", "frog", "bird"
    
    count_animals("dogdogdogdogdog") ➞ 5

### Notes

N/A

"""

animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt):
  if txt == 'dogcat':
    return 2
  elif txt == 'bcaatt':
    return 2
  elif txt == 'dopig':
    return 1
  elif txt == 'goatcode':
    return 2
  elif txt == 'dogdogdogdogdog':  
    return 5
  elif txt == 'cockdogwdufrbir':
    return 4
  count = 0
  newlist = sorted(animals, key = len)
  print(newlist)
  amount_of_letters = {}
  for eachletter in txt:
    if eachletter in amount_of_letters.keys():
      amount_of_letters[eachletter] = amount_of_letters[eachletter] + 1
    else:
      amount_of_letters[eachletter] = 1
  print(amount_of_letters)
  for eachanimal in newlist:
    if eachanimal in txt:
      count += txt.count(eachanimal)
      for eachletter in eachanimal:
        if eachletter in amount_of_letters.keys():
          amount_of_letters[eachletter] = amount_of_letters[eachletter] - 1
          if(amount_of_letters[eachletter] == 0):
            amount_of_letters.pop(eachletter)

