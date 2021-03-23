"""


Once you've learned how to select everything from a table in **SQL** , you can
start narrowing your search for _specific_ pieces of data with conditions. For
example, to select the data in a specific column, you can use this syntax.

    SELECT ColumnName FROM Table
    WHERE OtherColumn == 100;

In this challenge, fill in the query in the **Code** tab to select the data
from the `Name` column having `Salary` **greater than 45000** from the table
`employees` (see **Tests** tab).

### Original Table

Name| Salary  
---|---  
Adam| 50000  
Bob| 30000  
Charlotte| 45000  
Dillon| 70000  
Eileen| 70000  
Mubashir| 47000  
Joshua| 95000  
  
### Expected Results

Name  
---  
Adam  
Dillon  
Eileen  
Mubashir  
Joshua  
  
### Notes

  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * When presented with more complex queries like this, it is best practice to format your code by putting each statement on separate lines!
  * This challenge was heavily inspired by [Joshua Señoron's challenge](https://edabit.com/challenge/ThqPYNrRpXo9BHrwH) on SQL queries!

"""

query = "Select name from employees where  Salary >45000"

