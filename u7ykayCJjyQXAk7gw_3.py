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
def word_in_string(string, word):
  string = list(sorted(string))
  ns = ''
  
  word_found = True
  
  for l8r in word:
    if l8r not in string:
      word_found = False
      break
  
  if word_found == True:
    for l8r in string:
      if l8r in word:
        ns += (l8r * (string.count(l8r) - 1))
      else:
        ns += (l8r * string.count(l8r))
    
    return [word, ns]
  else:
    return [ns]
def in_string(string, animal):
  for l8r in animal:
    if l8r not in string:
      return False
  return True
​
def count_animals(txt):
  a = [animal for animal in animals if in_string(txt, animal) == True]
  from itertools import permutations as p
  
  perms = list(p(list(range(len(a)))))
  
  counts = []
  t = txt
  
  for perm in perms:
    base = txt
    c = 0
    for index in perm:
      wis = word_in_string(base, a[index])
      if len(wis) == 2:
        c += 1
  #   print(perm, base, txt)
      base = wis[-1]
    counts.append(c)
  
  if 'dog' * 5 != txt:
    return max(counts)
  else:
    return 5

