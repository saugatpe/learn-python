#class for the student
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

#str function
    def __str__(self):
        return f"{self.name} from {self.house}"

#to get input for user of name and house
@classmethod
def get(cls):
    name = input("name: ")
    house = input("house: ")
    return cls(name, house)

def main():
    student = Student.get()
    print(student)


#to run the above fucntion
if __name__ == "__main__":
    main()