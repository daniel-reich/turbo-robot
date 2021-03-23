"""


Create a function that determines the age difference between spouses in a
household. The ages `ages` in years of the parents and their children are
given in a list.

If there is no difference in age between the parents, return `"No age
difference between spouses."`. Otherwise, return the difference in years.
Check the examples for more clarification.

### Examples

    age_difference([29, 1, 6, 8, 28]) ➞ "1 year"
    
    age_difference([43, 86, 49, 86]) ➞ "No age difference between spouses."
    
    age_difference([2, 4, 6, 32, 27]) ➞ "5 years"

### Notes

  * Note the singular "year".
  * The younger spouse (if the spouses are not the same age) will be older than their oldest child by a minimum of 20 years.
  * The age difference between spouses will not be more than 18 years.

"""

def age_difference(ages):
  a, b  = sorted(ages)[-2:]
  diff  = b - a
  return "No age difference between spouses." if diff == 0 else '{} year{}'.format(diff, ('s', '')[diff == 1])

