"""


In SQL, the **COUNT()** function returns the number of rows that match a
specified criterion. You can use this syntax:

    SELECT COUNT(column_name)
    FROM table_name
    WHERE condition;

In this challenge, fill in the query in the **Code** tab to **COUNT** the
total visitors from the `Name` column, having `Bill` **greater than 10000**
_AND_ number of `Visits` **less than 15** from the table `Customers` (see
**Tests** tab).

### Original Table

Name| Bill| Visits  
---|---|---  
Mubashir| 25000| 29  
Joshua| 30000| 37  
Adam| 50000| 10  
Bob| 30000| 15  
Charlotte| 20000| 14  
Dillon| 15000| 13  
Eileen| 9000| 14  
  
### Expected Results

Count() = 3

### Notes

  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * When presented with more complex queries like this, it is best practice to format your code by putting each statement on separate lines!
  * You can try previous challenges [here](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)!

"""

query = """
SELECT COUNT(Name) FROM Customers
WHERE Bill>10000 AND Visits<15
"""

