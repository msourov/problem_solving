class Person:
    def __init__(self, person_name: str, year_of_birth: int, height_inches: int = None):
        self.__name = person_name  #__ is equivalent to declaring private in java
        self.__birth_year = year_of_birth
        self.__ht = height_inches

    def get_name(self):
        return self.__name

    def get_birth_year(self):
        return self.__birth_year

    def set_name(self, new_name):
        if self.__has_any_number(new_name): #Check if person name consists only of letters
            print('Sorry person name can\'t have number')
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return any(char.isdigit() for char in string)

    def get_summary(self):
        return f'Name: {self.__name}, YOB: {self.__birth_year}, Height: {self.__ht}'

class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name: {self.get_name()}, Email: {self.email}, Birth: {self.get_birth_year()}"

    def __str__(self):
        return self.get_summary()

    def __repr__(self):
        return self.get_summary()

class PlainClass: #A structure like class
    pass


if __name__ == '__main__':
    person_list = [Person('Mahmud', 1990, 172),
                   Person('Hasan', 1991, 171),
                   Person('Sourov', 1998, 169),
                   Person('Max', 1970, 175),
                   Person('John', 1998)]
    # for person in person_list:
    #     if person.get_birth_year() >= 1990:
    #         print(person.get_summary())
    student = Student('A', 2000, 'a@gmail.com', '181129')
    print(student)
    student.set_name('Hasan')
    print(student)
    abc = PlainClass()
    abc.name = 'Struct Like Class'
    print(abc.name)