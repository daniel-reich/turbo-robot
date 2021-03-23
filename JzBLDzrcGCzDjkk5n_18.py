"""


Make a function that encrypts a given input with these steps:

Input: `"apple"`

 **Step 1:** Reverse the input: `"elppa"`

 **Step 2:** Replace all vowels using the following chart:

    a => 0
    e => 1
    i => 2
    o => 2
    u => 3
    
    # "1lpp0"

 **Step 3:** Add "aca" to the end of the word: `"1lpp0aca"`

Output: `"1lpp0aca"`

### Examples

    encrypt("banana") ➞ "0n0n0baca"
    
    encrypt("karaca") ➞ "0c0r0kaca"
    
    encrypt("burak") ➞ "k0r3baca"
    
    encrypt("alpaca") ➞ "0c0pl0aca"

### Notes

All inputs are strings, no uppercases and all output must be strings.

"""

def encrypt(word):
  reverse_word= word[::-1]
  print(word,"word")
  print(reverse_word,"reverse_word")
  reverse_word=reverse_word.replace("a","0")
  reverse_word=reverse_word.replace("e","1")
  reverse_word=reverse_word.replace("o","2")
  reverse_word=reverse_word.replace("u","3")
  reverse_word+="aca"
  print(reverse_word,"reverse_word")
  return reverse_word

