"""


Create a function that takes in a _current mood_ and return a sentence in the
following format: `"Today, I am feeling {mood}"`. However, if _no argument_ is
passed, return `"Today, I am feeling neutral"`.

### Examples

    mood_today("happy") ➞ "Today, I am feeling happy"
    
    mood_today("sad") ➞ "Today, I am feeling sad"
    
    mood_today() ➞ "Today, I am feeling neutral"

### Notes

Check the **Resources** tab for some helpful information.

"""

def mood_today(mood = 'neutral'):
  return 'Today, I am feeling {}'.format(mood)

