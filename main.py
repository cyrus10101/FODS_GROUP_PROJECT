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
    
    def login_ui(self):
        print("________________________________________________________________")

    def sign_in(self):
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

    def user_un_exist(self):
            with open(self.__passwordfile, 'r') as checkfile:
                for line in checkfile:
                    username, password = line.strip().split
                     if username == self.username():
                        return " username already exist"
    def sign_up(self):
        while True:
            try:
                self.username = input('Usename: ')
                if len(self.username) < 3:
                    raise Exception(" Username must be at least more than 2 character")
                
                self.password = input('password: ')
                if len(self.password) < 5:
                    raise Exception (" pssword must be at least more than 4 character.")
                if not any(char.isalpha() for char in self.username) and not any(char.isdigit() for char in self.username):
                    raise Exception (" Password must consist alphabet and numbers.")
                break

            except Exception as e:
                print(f'Error! {e}')
        while True:
            try:
                with open(self.__passwordfile, 'w') as file:
                    self.check_un_exist()
                    with open(self.__passwordfile, 'r') as checkfile:
                        for line in checkfile:
                            username, password = line.strip().split
                            if username == self.username():
                                raise Exception(" username already exist")
                    


            except FileNotFoundError:
                print('Error! file not found.')
            except PermissionError:
                print('Error! Premission denied to wirte in this file')
            except Exception as e:
                print(f'Error! {e}')



    def login(self):
        self.login_ui()
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.sign_in()
            if choice == '2':
                self.sign_up()
            if choice == '0':
                return


    def add_student(self):

        try:
            with open(self.__userfile, 'a') as file:
                with open(self.__userfile, 'r') as checkfile:

    def update_student(self):
    def modify_student(self):
    def delete_student(self):
    def update_profile(self):

class Admin:
    def __init__(self, instance):
        self.object = instance
    def admin_ui(self):
        print("___________________________________________________________________________")
    def mainpage(self):
        while True:
            self.object.login()
            self.admin_ui()
            choice = input('Yout choice: ')
            if choice == '1':
                self.object.add_student()
            if choice == '2':
                self.object.update_student()
            if choice == '3':
                self.object.modify_student()
            if choice == '4':
                self.object.delete_student()
            if choice == '0':
                return

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
    if choice == '0':
        break

    user.mainpage()


