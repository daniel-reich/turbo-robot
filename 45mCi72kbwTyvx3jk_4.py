"""


Welcome to the series of SQL challenges, Juan has just entered the climate
research center and he needs to find the cities that start with a capital
letter B and end with the letter s, and most sort them in alphabetical order.

His friend tells him that he can use the LIKE method to find the matches in
the database and the ORDER BY function.

    SELECT name FROM population
    WHERE name LIKE 'a%'
    ORDER BY name asc

  * In this example, this query selects all the names which begin with an "a".
  * The percent symbol is a wild card which represents any characters.

  * In our first challenge we are going to **select everything** from the database `Station`, where the `City` starts with the letter "B" and end with the letter "s". Remember to order the results alphabetically.

### Original Table

    [
      ("New York", 0),
      ("Medellín", 24),
      ("Buenos Aires", 30),
      ("Madrid", 9),
      ("Chicago", -4),
      ("Brusellas", 4),
      ("Paris", 4)
    ]

### Expected Results

    [
      ("Brusellas", 4)
      ("Buenos Aires", 30)
    ]

### Notes

If you are stuck, remember to take a look at the **Resources** tab.

"""

query="""   
SELECT * FROM Station WHERE City LIKE 'B%' ORDER BY City asc
"""

