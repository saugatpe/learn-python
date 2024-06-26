#class for the student
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

#str function
    def __str__(self):
        return f"{self.name} from {self.house}"
    

    #getter for the name property
    @property 
    def name(self):
        return self._name

#setter for the name property
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name



#getter for the house property
    @property
    def house(self):
        return self._house
    

    #setter for the house property
    @house.setter
    def house(self, house):
        if house not in ["griffindor","Ravenclaw","slytherine"]:
                raise ValueError("Invalid house")
        self._house = house
    

#main function
def main():
    student = get_students()
    student._house = "Number four, privet driven"
    print(student)

#to get input for user of name and house
def get_students():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


#to run the above fucntion
if __name__ == "__main__":
    main()