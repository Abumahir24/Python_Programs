"""Question instruction:
Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.
Create a GitHub repository for your assignment and submit the link. """

class Person: #class declaration
    def introduce(self,name,age,gender): #construtor
        self.name=name
        self.age=age
        self.gender=gender
        print('This person is',name,'whose age is',age,'and gender is',gender)

#object creation
person=Person()
#access information
person.introduce('Ashraf Kweka',35,'male')

