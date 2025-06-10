# filepath: /Users/Chris/leet_code/learingclass.py
# Learning classes demonstration: Student tracks GPA stats; Microwave simulates appliance

class Student:
    # Class variables to track number of students and total GPA
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        # Initialize a Student instance with name and GPA
        self.name = name
        self.gpa = gpa
        # Update class-level statistics
        Student.count += 1
        Student.total_gpa += gpa
    
    def get_info(self):
        # Return a formatted string with the student's name and GPA
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        # Return the total number of Student instances created
        return f"Total students created: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        # Calculate and return the average GPA, or a message if none exist
        if cls.count == 0:
            return "No students available to calculate average GPA"
        average_gpa = cls.total_gpa / cls.count
        return f"Average GPA of all students: {average_gpa:.2f}"
    
class Microwave:
    # Represents a microwave with a brand, power rating, and on/off status

    def __init__(self, brand, power_rating, status) -> None:
        # Initialize microwave attributes: brand name, power rating, and status (True=on, False=off)
        self.brand = brand
        self.power_rating = power_rating
        self.status = status
    
    def turn_on(self) -> str:
        # Turn the microwave on if it's off; otherwise inform it's already on
        if self.status:
            return f"The microwave {self.brand} is already on"
        else:
            self.status = True
            return f"The microwave {self.brand} is now on"
    
    def turn_off(self) -> str:
        # Turn the microwave off if it's on; otherwise inform it's already off
        if not self.status:
            return f"The microwave {self.brand} is already off"
        else:
            self.status = False
            return f"The microwave {self.brand } is now off"
            
    def run(self, time) -> None:
        self.time = time
        if self.status == False:
            print(f"you need to first turn the microwave {self.brand}")
        else:
            print(f"the micrwave {self.brand} has been running for {self.time}")
            self.status = False
            print("your microwave is now off")

    def __add__ (self, other):
        print("what are you doing?")
            
# Example usage of the classes
smeg: Microwave = Microwave("Smeg", "B", False)   # Create a microwave instance in 'on' status
bosch: Microwave = Microwave("bosch", "C", False)  # Create a microwave instance in 'off' status
     

smeg.run(30)
st_1 = Student('Chris', 5.0)          # Create first student
st_2 = Student('Lisa', 3.4)           # Create second student

print(Student.get_count())            # Print total number of students created
print(Student.get_average_gpa())      # Print average GPA of all students