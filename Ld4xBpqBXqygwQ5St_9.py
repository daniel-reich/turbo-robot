"""


Your task is to write a program which allows teachers to create a _multiple
choice test_ in a class called `Testpaper` and to be also able to assign a
_minimum pass mark_. The testpaper's subject should also be included. The
attributes are in the following order:

  1. `subject`
  2. `markscheme`
  3. `pass_mark`

As well as that, we need to create student objects to take the test itself!
Create another class called `Student` and do the following:

  * Create an attribute called `tests_taken` and set the default as `'No tests taken'`.
  * Make a method called `take_test()`, which takes in the testpaper object they are completing and the student's answers. Compare what they wrote to the mark scheme, and **append to the/create a** dictionary assigned to `tests_taken` in the way as shown in the point below.
  * Each key in the dictionary should be the _testpaper subject_ and each value should be a string in the format seen in the examples below ( _whether or not the student has failed, and their percentage in brackets)_.

### Examples

    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
    
    student1 = Student()
    student2 = Student()
    student1.tests_taken ➞ "No tests taken"
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
    
    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

### Notes

  * Round percentages to the **nearest whole number**.
  * Remember that the attribute `tests_taken` should return 'No tests taken' when no tests have been taken yet.

"""

class Testpaper:
    subject = None
    markscheme = None
    pass_mark = None
    def __init__(self,sub,mark,pass_mark):
        self.subject = sub
        self.markscheme=mark
        self.pass_mark=pass_mark
​
class Student:
    tests_taken = None
    def __init__(self):
        self.tests_taken = 'No tests taken'
    def take_test(self, test, answers):
        fullscore = len(test.markscheme)
        resultat = 0
        for x,y in enumerate(answers):
            if test.markscheme[x] == y:
                resultat+=1
        score='{}%'.format(round((resultat / fullscore)*100),0)
        if type(self.tests_taken) == str:
            self.tests_taken={}
        if score > test.pass_mark:
            self.tests_taken[test.subject] = 'Passed! ({})'.format(score)
        else:
            self.tests_taken[test.subject] = 'Failed! ({})'.format(score)

