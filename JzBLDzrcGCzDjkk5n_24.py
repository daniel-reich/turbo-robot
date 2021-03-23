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
  rev = word[::-1]
  new=""
  i=0
  while i<len(rev):
    if rev[i]=="a":
      new=new+"0"
    elif rev[i]=="e":
      new=new+"1"
    elif rev[i]=="o":
      new=new+"2"
    elif rev[i]=="u":
      new=new+"3"
    else:
      new=new+rev[i]
    i=i+1
  new=new+"aca"
  return new

