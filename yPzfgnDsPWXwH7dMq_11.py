"""


Your task is to create a `class` to handle paginated content in a website. A
pagination is used to divide long lists of content in a series of pages.

![Example](https://s3.amazonaws.com/edabit-challenges/persons_paginated.png)

The pagination `class` will accept 2 parameters:

  1.  **items** (default: `[]`): A `list` of contents to paginate.

  2.  **pageSize** (default: `10`): The amount of items to show in each page.

So for example we could initialize our pagination like this:

    alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
    
    p = Pagination(alphabetList, 4)

And then use the method `getVisibleItems` to show the contents of the
paginated list.

    p.getVisibleItems() # ["a", "b", "c", "d"]

You will have to implement various methods to go through the pages such as:

  * `prevPage`
  * `nextPage`
  * `firstPage`
  * `lastPage`
  * `goToPage`

Here's a continuation of the example above using `nextPage` and `lastPage`:

    p.nextPage()
    
    p.getVisibleItems()
    # ["e", "f", "g", "h"]
    
    p.lastPage()
    
    p.getVisibleItems()
    # ["y", "z"]

### Notes

  * The second argument (`pageSize`) could be a `float`, in that case just convert it to an `int` (this is also the case for the `goToPage` method)
  * The methods used to change page should be chainable, so you can call them one after the other like this: `p.nextPage().nextPage()`
  * Please remove the comments I provided before publishing your solution.

"""

from math import ceil
​
class Pagination:
​
  def __init__(self, items=[], pageSize=10):
    self.items = items
    self.pageSize = pageSize
    self.totalPages = ceil(len(items)/pageSize)
    self.currentPage = 0
    
  def getItems(self):
    return self.items
    
  def getPageSize(self):
    return self.pageSize
    
  def getCurrentPage(self):
    return self.currentPage + 1
    
  # Goes to the previous page
  def prevPage(self):
    if self.currentPage > 0: self.currentPage -= 1
    return self
    
  # Goes to the next page
  def nextPage(self):
    if self.currentPage < self.totalPages-1: self.currentPage += 1
    return self
    
  # Goes to the first page
  def firstPage(self):
    self.currentPage = 0
    return self
    
  # Goes to the last page
  def lastPage(self):
    self.currentPage = self.totalPages-1
    return self
    
  # Goes to a page determined by the `page` argument
  def goToPage(self, page):
    page = int(page) - 1
    self.currentPage = 0 if page < 0 else self.totalPages-1 if page >= self.totalPages else page
    return self
    
  # Returns the currently visible items as an array
  def getVisibleItems(self):
    start = self.currentPage * self.pageSize
    return self.items[start:(start + self.pageSize)]
