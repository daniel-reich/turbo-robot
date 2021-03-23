"""


Create a function that takes a phrase and transforms each word using the
following rules:

  1. Keep first and last character the same.
  2. Transform middle characters into a dash `-`.

### Examples

    partially_hide("skies were pretty") ➞ "s---s w--e p----y"
    
    partially_hide("red is not my color") ➞ "r-d is n-t my c---r"
    
    partially_hide("She rolled her eyes") ➞ "S-e r----d h-r e--s"
    
    partially_hide("Harry went to fight the basilisk") ➞ "H---y w--t to f---t t-e b------k"

### Notes

Words with two or fewer letters should not be hidden at all.

"""

def partially_hide(phrase):
  phrase = phrase.split()
  counter=0
  while counter <= (len(phrase))-1:
    if len(phrase[counter]) <= 2:
      counter=counter+1
    else:
      nes=phrase[counter]
      counter1=nes[0]
      print(counter1)
      counter2=nes[-1]
      print(counter2)
      counter3= "-"*(len(nes)-2)
      print(counter3)
      counter1=counter1+counter3+counter2
      print(counter1)
      phrase[counter] = phrase[counter].replace(nes,counter1)
      counter=counter+1
  return ' '.join(phrase)

