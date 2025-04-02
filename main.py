import os
import time
class StudentManagementSystem:
    def __init__(self):
        self.userfile = "user.txt"
        self.gradefile = "grades.txt"
        self.ecafile = "eca.txt"
        self.adminfile= "admin_password.txt"
        self.studentfile = "student_password.txt"
        self.username = None
        self.password = None
        self.goback = False

    def timer(self, seconds):
        time.sleep(seconds)

    def clscr(self):
        #os.system(what_to_run if else)
        os.system('cls' if os.name =='nt' else 'clear')

    def ui(self):
        self.clscr()
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
    
    def empty_content(self, passfile):
        with open(passfile, 'r') as file:
            content = file.read().strip()
            if not content: 
                return True
            else:
                return False
            
    def goto_sign_up(self, passfile):
        choice = input('Do you want to sign up First(Y/N): ')
        if choice.lower() == 'y':
            self.sign_up(passfile)
        elif choice.lower() == 'n':
            self.login()
        else:
            print("Invalid chioce!")

    def attempt_fail(self, page):
        if page == self.adminfile:
            self.login(1)
        else:
            self.login(2)

    def sign_in(self, passfile):
        attempt = 5
        correct_userpass = False
        while True:
            self.username = input('Username: ')
            self.password = input('Password(case sensetive): ')
            try:
                if self.empty_content(passfile):        
                    print('Empty Database!')
                    self.goto_sign_up(passfile)
                with open(passfile, 'r') as file:
                    for line in file:
                        username, password = line.strip().split(":")
                        if self.username.lower() == username and self.password == password:
                            correct_userpass = True

                    if correct_userpass :
                        print("✅ Login succesfull.")
                        return                              
                    else:
                        print('\033[31mIncorrect username/password! Please try again.\033[0m')
                        attempt -= 1

                        if attempt <= 0:
                            print("\033[31mToo many failed attempts! Try again later\033[0m")
                            self.timer(2)
                            self.attempt_fail(passfile)
                            
            except FileNotFoundError:
                with open(passfile, 'x') as file:
                    print('file not found\nfile created.')
                self.sign_in(passfile) 
                print('Database is empty!')
            except Exception as e:
                print(f'Error {e}')

    def check_username_exist(self, passfile):
        with open(passfile, 'r') as checkfile:
            #checkfile.seek(0)
            content = checkfile.read().strip()
            for line in content.split("\n"):
                username, password = line.strip().split(":")
                if username == self.username:
                    return True
                
class Admin(StudentManagementSystem):
    def __init__(self):
        super().__init__()  # Call parent class's __init__

    def admin_ui(self):
        self.clscr()
        print(" =============================================================")
        print("|                          Admin page                         |")
        print(" =============================================================")
        print("|                                                             |")
        print("|                      Press '1' to add student               |")
        print("|                                                             |")
        print("|                      Press '2' to Sign Up                   |")
        print("|                                                             |")
        print("|                      Press '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")

    def admin_sign_up(self, passfile):
        while True:
            try:
                self.username = input('Username: ')
                if len(self.username) < 3:
                    raise ValueError ("\033[31mError! Username must be at least more than 2 character\033[0m")
                
                self.password = input('password: ')
                if len(self.password) < 5:
                    raise ValueError ("\033[31mError! pssword must be at least more than 4 character.\033[0m")
                if not any(char.isalpha() for char in self.password) or not any(char.isdigit() for char in self.password):
                    raise ValueError ("\033[31mError! Password must consist alphabet and numbers.\033[0m")
                
                with open(passfile, 'a') as file:
                    if not self.empty_content(passfile):
                        if self.check_username_exist(passfile):
                            raise ValueError ("\033[31mError! Username already exist.\033[0m") 
                        
                    file.write(f"{self.username}:{self.password}\n")
                    print("✅ Sign up succesfull.")
                    self.timer(2)
                    break

            except FileNotFoundError:
                print('Error! file not found.')
            except PermissionError:
                print('Error! Premission denied to wirte in this file')
            except Exception as e:
                print(f'{e}')
                
    def admin_login(self):
        self.login_ui(1)
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.sign_in(self.adminfile)
                return
            if choice == '2':
                self.admin_sign_up(self.adminfile)
                return
            if choice == '0':
                self.goback = True
                return

    def mainpage(self):
        while True:
            self.admin_login()
            if self.goback:
                return
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
        user = Admin()
    if choice == '2':
        user = Student(studentmanagementsystem)
    if choice == '0':
        break

    user.mainpage()