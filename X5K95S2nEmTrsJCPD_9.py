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
  if 'smile' in txt:
    return "Make me :D"
  elif 'grin' in txt:
    return 'Make me :)'
  elif 'sad' in txt:
    return 'Make me :('
  elif 'mad' in txt:
    return 'Make me :P'

