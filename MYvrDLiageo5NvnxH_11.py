"""


In order to improve your Python skills, you decide to go to an online
bookstore that exclusively sells beginner Python books. You can search through
the site by setting the `param` variable to a string containing your
keyword(s); however, you notice that an error is thrown whenever your search
contains a double quote.

You look through the site's Python code and notice that it uses `exec()` to
set the result of your search to a variable named `res`. Create a query that
copies the `users` dictionary (containing everyone's username and password) to
`res`.

### Examples

    param = "your text here"
    
    users = {
      "user1": "password",
      "user2": "password"
    }
    
    exec("res = search('%s')" % param)
    
    print(res) ➞ users

### Notes

  * Create a string, not a function.
  * The rest of the Injection challenges can be [found here](https://edabit.com/collection/dnXtkLPZpX25t227q).

"""

param = "\");res=users #"

