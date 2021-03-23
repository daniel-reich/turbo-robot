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
  return txt.replace('smile',':D') if 'smile' in txt else txt.replace('grin',':)') if 'grin' in txt else txt.replace('sad',':(') if 'sad' in txt else txt.replace('mad',':P')

