"""


Write a function that takes a string of one or more words as an argument and
returns the same string, but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces. Spaces will be
included only when more than one word is present.

### Examples

    reverse("Reverse") ➞ "esreveR"
    
    reverse("This is a typical sentence.") ➞ "This is a lacipyt .ecnetnes"
    
    reverse("The dog is big.") ➞ "The dog is big."

### Notes

You can expect a valid string to be provided for each test case.

"""

def reverse(txt):
  return_string = ''
  txt_new = list(txt.split(' '))
  for i in range (len(txt_new)):
    output_string=''
    lst_txt = str(txt_new[i])
    
    for j in range (len(lst_txt)):
      if(len(lst_txt)>=5):
        output_string+=lst_txt[len(lst_txt)-1-j]
      else:
        output_string+=lst_txt[j]
      
    if (i==0):
      return_string = output_string
    else:
      return_string = return_string + ' ' + output_string
  return return_string

