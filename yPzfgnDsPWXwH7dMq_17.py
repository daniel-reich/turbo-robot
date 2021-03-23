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

class Pagination:
    def __init__(self,x=[],y=10):
        self.items = x
        self.pageSize = y
        self.curr = [self.items[i] for i in range(self.pageSize)] if self.items != [] else [] 
        self.currpage = 1
        self.endpage = (len(self.items)//self.pageSize) + 1 if (len(self.items)%self.pageSize!=0) else (len(self.items)//self.pageSize)
​
        
    def getPageSize(self):
        return self.pageSize
    def getItems(self):
        return self.items
​
    def getVisibleItems(self):
        start = self.pageSize * self.currpage - self.pageSize
        end = min(self.pageSize * self.currpage,len(self.items))
        self.curr = [self.items[i] for i in range(start,end)]
        return self.curr
    def getCurrentPage(self):
        return self.currpage
​
    def nextPage(self):
        self.currpage += 1
        if self.currpage > self.endpage:
            self.currpage = self.endpage
        return self
    def lastPage(self):
        self.currpage = self.endpage
        return self
    def prevPage(self):
        self.currpage -= 1
        if self.currpage == 0:
            self.currpage = 1
        return self
    def firstPage(self):
        self.currpage = 1
        return self
    def goToPage(self,num):
        num = int(num)
        if num*self.pageSize > len(self.items):
            return self.lastPage()
        if num < 1:
            return self.firstPage()
        self.currpage = num
        return self

