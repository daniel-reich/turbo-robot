"""


Given a _dictionary_ of some items with _star ratings_ and a _specified star
rating_ , return a new dictionary of items **which match the specified star
rating**. Return `"No results found"` if _no item_ matches the _star rating_
given.

### Examples

    filter_by_rating({
      "Luxury Chocolates" : "*****",
      "Tasty Chocolates" : "****",
      "Aunty May Chocolates" : "*****",
      "Generic Chocolates" : "***"
    }, "*****") ➞ {
      "Luxury Chocolates" : "*****",
      "Aunty May Chocolates" : "*****"
    }
    
    filter_by_rating({
      "Continental Hotel" : "****",
      "Big Street Hotel" : "**",
      "Corner Hotel" : "**",
      "Trashviews Hotel" : "*",
      "Hazbins" : "*****"
    }, "*") ➞ {
      "Trashviews Hotel" : "*"
    }
    
    filter_by_rating({
      "Solo Restaurant" : "***",
      "Finest Dinings" : "*****",
      "Burger Stand" : "***"
    }, "****") ➞ "No results found"

### Notes

N/A

"""

def filter_by_rating(d, rating):
    answer = {x:d[x] for x in d if d[x] == rating}
    return answer if answer else 'No results found'

