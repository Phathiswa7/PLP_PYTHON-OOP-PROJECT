# Define the Person class
class Person:
    # Initialize the Person object with name, age, and gender attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person_instance = Person(name="Alex", age=25, gender="Male")

# Call the introduce method
person_instance.introduce()
