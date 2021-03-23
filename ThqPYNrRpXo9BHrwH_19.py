"""


Once you've learned how to select everything from a table in **SQL** , you can
start narrowing your search for _specific_ pieces of data. For example, to
select the data in a specific column, you can use this syntax.

    SELECT ColumnName FROM Table;

  * Instead of using the asterisks like in the previous exercise, we can choose to select a specific column instead.

In this challenge, fill in the query in the **Code** tab to select the data
from the `Name` column from the table `employees` (see **Tests** tab).

### Original Table

Name| Salary  
---|---  
Adam| 50000  
Bob| 30000  
Charlotte| 45000  
Dillon| 70000  
Eileen| 70000  
  
### Expected Results

Name  
---  
Adam  
Bob  
Charlotte  
Dillon  
Eileen  
  
### Notes

  * Check the **Resources** tab for more SQL tutorials and exercises.
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

query = "SELECT Name FROM Employees;"

