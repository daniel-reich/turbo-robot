"""


In many cases, **SQL** is used to select more than just columns in a table.
For example, you can filter your search by specifying conditions as seen
below:

    SELECT * FROM Table
    WHERE Name = "Bob";

  * Again, we can use the asterisks to select all the data in a table.
  * However, with the use of the WHERE keyword, only all of Bob's data is selected.

Name| Salary  
---|---  
Bob| 30000  
  
In this challenge, fill in the query in the **Code** tab to select the
`Salary` from "Adam" in the `Employees` table.

### Original Table

Name| Salary  
---|---  
Adam| 50000  
Bob| 30000  
Charlotte| 45000  
Dillon| 70000  
Eileen| 70000  
  
### Expected Results

Salary  
---  
50000  
  
### Notes

  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * When presented with more complex queries like this, it is best practice to format your code by putting each statement on separate lines!
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

query = " SELECT Salary FROM Employees WHERE Name='Adam'"

