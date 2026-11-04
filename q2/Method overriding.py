ACTIVITY 1: Method overriding in a Zoo Management System.
—-------------
Allotted Time: 30 minutes
Grading: Non-graded, but a submission is required.
Submission: Upload your file to the Khub submission bin.
File Name: Follow the file name format to be provided by your teacher

Instructions:
1. Create the Python code that creates the parent class, Animal, and the child classes: Lion,
Elephant, and Monkey, based on the given class diagram.

class Animal:
    def __init__(self, name: str):
        self._name = name  # Private attribute in class diagram yisyiss rahhhh - name: str
    @property
    def eat(self):
        pass
    @property
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return f"{self._name}# roars Trex rahhh!!
        
       
       



2. Override the eat() and make_sound() methods of the parent class Animal in the
child classes: Lion, Elephant, and Monkey, to output the appropriate behavior of the animal.
The lion roars loudly; the lion eats fresh meat.
The elephant trumpets; the elephant eats grass and fruits.
The monkey chatters; the monkey eats bananas.
The object’s name must be included in the output texts, as shown below.
3. Create an object for each child's class and call the methods using a for loop.

