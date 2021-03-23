"""


Write a function that removes all capitals letters from a sentence except the
first letter, put quotation marks around the sentence and add _", whispered
Edabit."_ at the end.

### Examples

    shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'
    
    shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'
    
    shhh("") ➞ '"", whispered Edabit.'

### Notes

Don't forget to surround the original string with double quotation marks `""`.

"""

def shhh(txt):
  return '"{}"'.format(txt.capitalize())+", whispered Edabit."

