import os
import time
class StudentManagementSystem:
    def __init__(self):
        self.__userfile = "user.txt"
        self.__gradefile = "grades.txt"
        self.__ecafile = "eca.txt"
        self.__adminfile= "admim_password.txt"
        self.__studentfile = "student_password.txt"
        self.username = None
        self.password = None
    def timer(self, seconds):
        time.sleep(seconds)

    def clscr(self):
        #os.system(what_to_run if else)
        os.system('cls' if os.name =='nt' else 'clear')

    def ui(self):
        print(" =============================================================")
        print('|                   Student Management System                 |')
        print(" =============================================================")
        print("|                                                             |")
        print("|                   Press '1' for Admin login                 |")
        print("|                                                             |")
        print("|                  Press '2' for Student login                |")
        print("|                                                             |")
        print(" =============================================================")
    
    def login_ui(self, para):
        self.clscr()
        print(" =============================================================")
        if para == 1:
            print("|                    Admin Login page                         |")
        else:
            print("|                      Student Login Page                     |")
        print(" =============================================================")
        print("|                                                             |")
        print("|                      Press '1' to Sign In                   |")
        print("|                                                             |")
        print("|                      Press '2' to Sign Up                   |")
        print("|                                                             |")
        print("|                      Press '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")
    
    def goto_sign_up(self, passfile):
        choice = input('Do you want to sign up First(Y/N): ')
        if choice.lower() == 'y':
            self.sign_up(passfile)
        elif choice.lower() == 'n':
            self.login()
        else:
            print("Invalid chioce!")

    def sign_in(self, passfile):
        attempt = 5
        while True:
            self.username = input('Username: ')
            self.password = input('Password: ')
            try:
                with open(passfile, 'r') as file:
                    content = file.read().strip()
                    if not content:
                        print('Empty Database!')
                        self.goto_sign_up(passfile)

                    for line in content.split("\n"):
                        username, password = line.strip().split(":")
                        if self.username == username and self.password == password:
                            print("✅ Login succesfull.")
                            self.timer(2)
                            return 
                        else:
                            print('Incorrect username/password! Please try again.')
                            attempt -= 1

                        if attempt <= 0:
                            print("\033[31mToo many failed attempts! Try again later\033[0m")

            except FileNotFoundError:
                with open(passfile, 'x') as file:
                    print('file not found\nfile created.')
                self.sign_in(passfile) 
                print('Database is empty!')
            except Exception as e:
                print(f'Error {e}')

    def check_username_exist(self, passfile):
        with open(passfile, 'r') as checkfile:
            for line in checkfile:
                username, password = line.strip().split
                if username == self.username():
                    return True

    def sign_up(self, passfile):
        while True:
            try:
                self.username = input('Usename: ')
                if len(self.username) < 3:
                    raise ValueError (" Username must be at least more than 2 character")
                
                self.password = input('password: ')
                if len(self.password) < 5:
                    raise ValueError (" pssword must be at least more than 4 character.")
                if not any(char.isalpha() for char in self.username) and not any(char.isdigit() for char in self.username):
                    raise ValueError (" Password must consist alphabet and numbers.")
                
                with open(passfile, 'w') as file:
                    if self.check_username_exist(passfile):
                        raise ValueError (" Username already exist.") 
                    file.write(f"{self.username}:{self.password}")
                    print("✅ Sign up succesfull.")
                    break

            except FileNotFoundError:
                print('Error! file not found.')
            except PermissionError:
                print('Error! Premission denied to wirte in this file')
            except Exception as e:
                print(f'Error! {e}')

    def goback(self):
        return False
    
    def login(self, para):
        self.login_ui(para)
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.sign_in(self.__adminfile)
                return
            if choice == '2':
                self.sign_up(self.__adminfile)
                return
            if choice == '0':
                self.goback


class Admin:
    def __init__(self, instance):
        self.object = instance
    def admin_ui(self):
        print(" =============================================================")
        print("|                          Admin page                         |")
        print(" =============================================================")
        print("|                                                             |")
        print("|                      Press '1' to                    |")
        print("|                                                             |")
        print("|                      Press '2' to Sign Up                   |")
        print("|                                                             |")
        print("|                      Press '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")

    def mainpage(self):
        while True:
            self.object.login(1)
            if self.object.goback:
                self.mainpage()

            self.admin_ui()
            choice = input('Yout choice: ')
            if choice == '0':
                return

class Student:
    def __init__(self, instance):
        self.object = instance
    def mainpage(self):
        pass

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


