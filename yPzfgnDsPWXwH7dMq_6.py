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

class Pagination(object):
​
    def __init__(self, items=[], pageSize=10):
        super(Pagination, self).__init__()
        self.items = items
        self.pageSize = int(pageSize)
        #splits items into lists the length of pageSize
        self.pages = [items[x:x+self.pageSize] for x in range(0, len(items), self.pageSize)]
        self.totalPages = len(self.pages)
        self.currentPage = 1
​
    def getItems(self):
        return self.items
​
    def getPageSize(self):
        if self.items == []:
            return 10
        else:
            return len(self.pages[self.currentPage-1])
​
    def getCurrentPage(self):
        return self.currentPage
​
    def prevPage(self):
        if self.currentPage == 1:
            pass
        else:
            self.currentPage -= 1
        return self
​
    def nextPage(self):
        if self.currentPage == len(self.pages):
            pass
        else:
            self.currentPage += 1
        return self
​
    def firstPage(self):
        self.currentPage = 1
        return self
​
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
​
    def goToPage(self, specificPage):
        if specificPage < 1:
            self.currentPage = 1
        elif specificPage > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = int(specificPage)
        return self
​
    def getVisibleItems(self):
        return self.pages[self.currentPage-1]

