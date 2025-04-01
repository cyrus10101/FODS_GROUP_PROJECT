class StudentManagementSystem:
    def __init__(self):
        self.__userfile = "user.txt"
        self.__gradefile = "grades.txt"
        self.__ecafile = "eca.txt"
        self.__passwordfile = "password.txt"
        self.username = None
        self.password = None
    def ui(self):
        print('_____________________________________________________\n')
    
    def login(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        while True:
            try:
                with open(self.__passwordfile) as file:
                    for line in file:
                        username, password = line.strip().split()
                        if self.username == username and self.password == password:
                            return
                        else:
                            print('Incorrect username/password! Please try again.')

            except FileNotFoundError:
                print('Database is empty!')
            except Exception as e:
                print(f'Error {e}')

    def add_student(self):
    def update_student(self):
    def modify_student(self):
    def delete_student(self):
    def update_profile(self):
class Admin:
    def __init__(self, instance):
        self.object = instance
    def admin_ui(self):
        
    def mainpage(self):
        self.object.login()

class Student:
    def __init__(self, instance):
        self.object = instance
    def mainpage(self):
        self.object.username 

studentmanagementsystem = StudentManagementSystem()
while True:
    studentmanagementsystem.ui()
    choice = input('Your choice: ')
    if choice == '1': 
        user = Admin(studentmanagementsystem)
    if choice == '2':
        user = Student(studentmanagementsystem)
    
    user.mainpage()


