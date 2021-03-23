"""


Once you've learned how to [SELECT
everything](https://edabit.com/challenge/ThqPYNrRpXo9BHrwH) from a table in
**SQL** , you can sort your results in ascending or descending order. By
default, SQL will always sort the results in ascending order. For example:

    SELECT * FROM Table
    ORDER BY ColumnName

... is the same as:

    SELECT * FROM Table
    ORDER BY ColumnName ASC

You can sort the results in descending order by using this syntax:

    SELECT * FROM Table
    ORDER BY ColumnName DESC

In this challenge, fill in the query in the **Code** tab to select **All
Data** from the table `Customers` sorted by the `Visits` column in **Ascending
Order** (see **Tests** tab).

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

Name| Bill| Visits  
---|---|---  
Adam| 50000| 10  
Dillon| 15000| 13  
Charlotte| 20000| 14  
Eileen| 9000| 14  
Bob| 30000| 15  
Mubashir| 25000| 29  
Joshua| 30000| 37  
  
### Notes

  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * When presented with more complex queries like this, it is best practice to format your code by putting each statement on separate lines!
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

query = """
select * from customers order by visits
"""

