"""


Write a function that takes a list of strings and a pattern (string) and
returns the strings that contain the pattern in **alphabetical order**. If the
pattern is an empty string, return all the strings passed in the input list.

### Examples

    cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]
    
    cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]
    
    cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]

### Notes

  * The given letter(s) are case insensitive and can be more than one.
  * In the case of an empty string, return the entire list.
  * A CMS is a Content Management System.

"""

def cms_selector(lst, txt):
    return sorted([e for e in lst if e.count(txt) > 0])

