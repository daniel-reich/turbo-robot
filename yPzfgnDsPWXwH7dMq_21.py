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

import math
​
class Pagination():
​
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.startPos = 0
        self.endPos = pageSize
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        return self.pageSize
​
    def getCurrentPage(self):
        return(math.ceil(self.endPos / self.pageSize))
​
    def getVisibleItems(self):
        return self.items[self.startPos:self.endPos]
​
    def prevPage(self):
        if self.startPos >= self.pageSize:
            self.endPos = self.endPos - self.pageSize
            self.startPos = self.startPos - self.pageSize
        return self
​
    def nextPage(self):
        if self.endPos <= len(self.items) - self.pageSize:
            self.endPos = self.endPos + self.pageSize
            self.startPos = self.startPos + self.pageSize
        elif self.endPos <= len(self.items):
            self.endPos = len(self.items)
            self.startPos = len(self.items) - len(self.items) % self.pageSize
        return self
​
    def firstPage(self):
        self.startPos = 0
        self.endPos = 3
        return self
​
    def lastPage(self):
        self.startPos = (len(self.items)) - (len(self.items) % self.pageSize)
        self.endPos = len(self.items)
        return self
​
    def goToPage(self, page):
        if page >= 1 and page <= int(len(self.items) / self.pageSize) + 1:
            self.startPos = int(page) * self.pageSize - self.pageSize
            self.endPos = int(page) * self.pageSize
        elif page > int(len(self.items) / self.pageSize) + 1:
            self.lastPage()
        elif page < 1:
            self.firstPage()
        return self

