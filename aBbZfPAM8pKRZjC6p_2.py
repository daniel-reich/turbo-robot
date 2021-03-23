"""


Fruit salads are served best when the fruits are sliced and diced into small
chunks!

For this challenge, slice each fruit **in half** and sort the chunks
**alphabetically.** This recipe tastes best when the chunks are **joined
together to make a string.**

###  Worked Example

    fruit_salad(["apple", "pear", "grapes"]) ➞ "apargrapepesple"
    
    # Chunks: ["ap", "ple", "pe", "ar", "gra", "pes"]
    # Sorted chunks: ["ap", "ar", "gra", "pe", "pes", "ple"]
    # Final string: "apargrapepesple"

### Examples

    fruit_salad(["apple", "pear", "grapes"]) ➞ "apargrapepesple"
    
    fruit_salad(["raspberries", "mango"]) ➞ "erriesmangoraspb"
    
    fruit_salad(["banana"]) ➞ "anaban"

### Notes

  * If a fruit has an odd number of letters, make the right side larger than the left.
  * For example: `"apple"` will be sliced into `"ap"` and `"ple"`.
  * All fruits will be given in lowercase.

"""

def fruit_salad(fruits):
  final_str = ''
  split_fruits = []
  for f in fruits:
    first_half, second_half = f[:len(f)//2],f[len(f)//2:]
    split_fruits.append(first_half)
    split_fruits.append(second_half)
  sort_split_fruits = sorted(split_fruits, key=str.lower)
  for split in sort_split_fruits:
    for s in split:
      final_str = ''.join((final_str, s))
      
  return final_str

