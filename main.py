import os
import time
class StudentManagementSystem:
    def __init__(self):
        self.userfile = "user.txt"
        self.gradefile = "grades.txt"
        self.ecafile = "eca.txt"
        self.adminfile= "admin_password.txt"
        self.studentfile = "student_password.txt"
        self.cfm_student = "confrom_student.txt"
        self.username = None
        self.password = None
        self.verify = None
        self.goback = False
        self.no_unique = False

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
            
    def sign_in(self, passfile):
        attempt = 5
        correct_userpass = False
        while True:
            self.username = input('Username: ')
            self.password = input('Password(case sensetive): ')
            try:
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
                            print("\033[31mToo many failed attempts! Try again later\nGoing back in 2 seconds\033[0m")
                            self.timer(2)
                            self.goback = True
                            return
                            
            except FileNotFoundError:
                print('\033[31mDatabase is empty!\nGoing back in 2 second\033[0m')
                self.timer(2)
                self.goback = True
                return
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
                
    def id_exist(self):
        with open(self.userfile, 'r') as file:
            for line in file:
                chk_verify, chk_name, chk_clss, chk_section = line.strip().split(":")
                if int(chk_verify) == self.verify:
                    return True
            return False    
    
    def check_verification(self):
        with open(self.cfm_student, 'r') as file:
            for line in file:
                id, chk_name, chk_clss, chk_section, chk_verify = line.strip().split(":")
                if chk_verify == self.verify:
                    return True
        return False   
    
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

    def choices_ui(self):
        pass

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
                    return

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
            

    def add_student(self):
        try:
            with open(self.userfile, 'r'), open(self.cfm_student, 'w'):
                pass
        except FileNotFoundError:
            with open(self.userfile, 'w'), open(self.cfm_student, 'w'):
                pass
        while True:
            try:
                name = input('Student Name: ')
                section = input('Section: ')
                clss = int(input('Level :'))
                id = int(input('Id: '))
                verification_id = input('Verification Id: ')
                self.verify = id
                if not self.empty_content(self.userfile):
                    if self.id_exist():
                        raise Exception (f"Id {self.verify} is already used.")
                with open(self.cfm_student, 'a') as file, open(self.userfile, 'a') as file2:
                    file.write(f"{id}:{name}:{clss}:{section}:{verification_id}\n")
                    file2.write(f"{id}:{name}:{clss}:{section}\n")
                    print('✅ Successfully Added student.')
                choice = input('Do you want to continue adding student(Y/N): ')
                if choice.lower() == 'y':
                    self.add_student()
                elif choice.lower() == 'n':
                    self.mainpage()
                else:
                    print('\033[31mInvalid input!\033[0m')

            except ValueError:
                print('\033[31mError! only digits are allowed to enter in level and Id\033[0m')
            except Exception as e:
                print(f'\033[31mError! {e}\33[0m')
    def update_personal(self):
        pass
    def update_marks(self):
        pass
    def update_eca(self):
        pass
    
    def update_record(self):
        self.choices_ui()
        choice = input('Your choice: ')
        if choice == '1':
            self.update_personal()
        elif choice == '2':
            self.update_marks()
        elif choice == '3':
            self.update_eca()
        else:
            print('\033[31mInvalid  Choice!\033[0m')

    def modify_record(self):
        pass
    def delete_record(self):
        pass

    def mainpage(self):
        while True:
            self.admin_login()
            if self.goback:
                return
            self.admin_ui()
            choice = input('Your choice: ')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_record()
            elif choice == '3':
                self.modify_record()
            elif choice == '4':
                self.delete_record()
            elif choice == '0':
                return
            else:
                print('\033[31mInvalid choice!\033[0m')

class Student(StudentManagementSystem):
    def __init__(self):
        super().__init__()
        
    def student_ui(self):
        pass

    def student_sign_up(self, passfile):
        while True:
            try:
                self.username = input('Username: ')
                if len(self.username) < 3:
                    raise Exception ("\033[31mError! Username must be at least more than 2 character\033[0m")
                self.password = input('Password: ')
                if len(self.password) < 5: 
                    raise Exception ("\033[31mError! Password must be more than 4 character.\033[0m")
                if not any(char.isalpha() for char in self.password) or not any(char.isdigit() for char in self.password):
                    raise Exception ("\033[31mError! Password must consist alphabet and numbers.\033[0m")
                id = input('verification Id: ')
                self.verify = id
                if not self.check_verification():
                    raise Exception ("\033[31mError! Verification id didn't match.\033[0m")
                with open(passfile, 'a') as file:
                    file.write(f"{self.username}:{self.password}")
                    print("✅ Sign up succesfull.")
                    self.timer(2)
                return
            
            except PermissionError: 
                print(f'Error! Permission denied to write in file')
            except Exception as e:
                print(f"{e}")

    def update_profile(self):
        pass
    def view_profile(self):
        pass
    def view_marks(self):
        pass
    def view_eca(self):
        pass
    def student_login(self):
        self.login_ui(2)
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.sign_in(self.studentfile)
                return
            elif choice == '2':
                self.student_sign_up(self.studentfile)
            elif choice == '0':
                self.goback = True
                return
            else:
                print('Invalid Choice!')

    def mainpage(self):
        while True:
            self.student_login()
            if self.goback:
                return
            self.student_ui()
            choice = input('Your chioce: ')
            if choice == '1':
                self.update_profile()
            elif choice == '2':
                self.view_profile()
            elif choice == '3':
                self.view_marks()
            elif choice == '4':
                self.view_eca()
            elif choice == '0':
                return 
            else:
                print('Invalid Choice!')

studentmanagementsystem = StudentManagementSystem()
while True:
    studentmanagementsystem.ui()
    choice = input('Your choice: ')
    if choice == '1': 
        user = Admin()
    if choice == '2':
        user = Student()
    if choice == '0':
        break

    user.mainpage()