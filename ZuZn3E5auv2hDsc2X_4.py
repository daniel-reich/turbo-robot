"""


 **SQL** is a great language on its own, but its functionality can be
empowered by **integrating** it into Python. For example, the `sqlite3`
library allows us to use Python **variables** in our databases, and to modify
tables during the runtime of a program.

 _In previous challenges, you may have seen queries structured like this..._

    SELECT * From Employee WHERE Salary > 30000

 _... Whereas when adding Python to the mix, you may see queries structured
like this!_

    salary = 30000
    c.execute("SELECT * From Employee WHERE Salary > ?", (salary,))
    employees = c.fetchall()

  1. Using **question marks as placeholders** , we can insert any variable into an SQL statement, much like how you might use the string `format()` method.
  2. `c` is the cursor for the database, and is the object we refer to whenever we need to execute statements or retrieve data.
  3. `c.fetchall()` is a method that returns a **list of tuples** containing the data queried from the SQL. For example, the output yielded from this statement could be this:

    [ ('Adam', 35000), ('Charlotte', 50000), ('Edgar', 60000) ]

### The Challenge

Create a function that returns the `Title` and `Pages` of books which
**strictly** have a **greater** number of pages than the given argument.

  * The data comes from the `Book` table.
  * Return a **list of tuples**.

### Examples

Title| Pages  
---|---  
Book A| 300  
Book B| 10  
Book C| 200  
Book D| 250  
      
    
    longer_than_n_pages(200) ➞ [("Book A", 300), ("Book D", 250)]

### Notes

  * It is generally agreed to use parameters, rather than using the `format()` method itself since they are intentionally designed to protect against SQL injection attacks.
  * Parameters in `sqlite3` must always be formatted in **tuples** , which is why you see the trailing comma in `(salary,)`. The comma ensures that the input is a tuple.
  * The cursor doesn't have to be named `c`, but it is for the purposes of this challenge.
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

def longer_than_n_pages(pages):
  c.execute("SELECT * FROM Book WHERE Pages > ?", (pages,))
  result = c.fetchall()
  return result

