"""


Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad` and `mad` with their
corresponding emoticons.

word| emoticon  
---|---  
smile| :D  
grin| :)  
sad| :(  
mad| :P  
  
### Examples

    emotify("Make me smile") ➞ "Make me :D"
    
    emotify("Make me grin") ➞ "Make me :)"
    
    emotify("Make me sad") ➞ "Make me :("

### Notes

  * The sentence always starts with "Make me".
  * Try to solve this **without** using conditional statements like **if/else**.

"""

def emotify(txt):
  txt = txt.split()
  D = {
  'smile': ':D',
  'grin': ':)',
  'sad': ':(',
  'mad': ':P',
  }
  for i, char in enumerate(txt):
    if char in D.keys():
      txt[i] = D[char]
  return ' '.join(txt)

