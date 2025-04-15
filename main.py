import os
import time
from cryptography.fernet import Fernet
import pandas as pd
from tabulate import tabulate

class StudentManagementSystem:
    def __init__(self):
        self.userfile = "user.txt"
        self.personalfile = 'personal.txt'
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
        print("|                   Enter '1' for Admin login                 |")
        print("|                                                             |")
        print("|                  Enter '2' for Student login                |")
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
        print("|                      Enter '1' to Sign In                   |")
        print("|                                                             |")
        print("|                      Enter '2' to Sign Up                   |")
        print("|                                                             |")
        print("|                      Enter '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")
    
    def gender_selector_ui(self):
        print('|----------------------------------------|')
        print("|            Enter 1 for male            |")
        print("|                                        |")
        print("|            Enter 2 for female          |")
        print("|                                        |")
        print("|            Enter 3 for others          |")
        print('|----------------------------------------|')

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
                        parts = line.strip().split(":")
                        # For student password file (format: id:username:password)
                        if passfile == self.studentfile and len(parts) == 3:
                            student_id, username, password = parts
                            if self.username.lower() == username.lower() and self.password == password:
                                self.verify = student_id  # Store the student ID
                                correct_userpass = True
                                break
                        # For admin password file (format: username:password)
                        elif len(parts) == 2:
                            username, password = parts
                            if self.username.lower() == username.lower() and self.password == password:
                                correct_userpass = True
                                break

                    if correct_userpass:
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
                print(f'\033[31mError {e}\033[0m')

    def check_username_exist(self, passfile):
        with open(passfile, 'r') as checkfile:
            content = checkfile.read().strip()
            if not content:
                return False
                
            for line in content.split("\n"):
                parts = line.strip().split(":")
                # For student password file (format: id:username:password)
                if passfile == self.studentfile and len(parts) == 3:
                    _, username, _ = parts
                    if username.lower() == self.username.lower():
                        return True
                # For admin password file (format: username:password)
                elif len(parts) == 2:
                    username, _ = parts
                    if username.lower() == self.username.lower():
                        return True
            return False

    def id_exist(self, passfile):
        with open(passfile, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if self.verify == int(line.split(':')[0]):
                    return True
        return False    
    
    def check_verification(self):
        with open(self.cfm_student, 'r') as file:
            for line in file:
                id, chk_name, chk_clss, chk_section, chk_verify = line.strip().split(":")
                if chk_verify == self.verify:
                    return True
        return False   
    
    # Check if file exist or not if not creates file.
    def check_file_exist(self, passfile):
        try: 
            with open(passfile, 'r') as file:
                pass
        except FileNotFoundError:
            with open(passfile, 'w') as file:
                pass

    def gender_selector(self, choice):
        if choice == '1':
            return 'Male'
        elif choice == '2':
            return 'Female'
        elif choice == '3':
            return 'Others'
        else:
            raise Exception("\033[31mPlease Choose Valid Gender\033[0m")

class Admin(StudentManagementSystem):
    def __init__(self):
        super().__init__()  # Call parent class's __init__

    def admin_ui(self):
        self.clscr()
        print(" =============================================================")
        print("|                          Admin page                         |")
        print(" =============================================================")
        print("|                                                             |")
        print("|                      Enter '1' to Add Student               |")
        print("|                                                             |")
        print("|                      Enter '2' to Update Record             |")
        print("|                                                             |")
        print("|                      Enter '3' to Modify Record             |")
        print("|                                                             |")
        print("|                      Enter '4' to Delete Record             |")
        print("|                                                             |")
        print("|                      Enter '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")

    def choices_ui(self):
        self.clscr()
        print(" -------------------------------------------")
        print("|                 RECORDS                   |")
        print("|                                           |")
        print("|        Enter '1' for personal info        |")
        print("|                                           |")
        print("|        Enter '2' for Grades               |")
        print("|                                           |")
        print("|        Enter '3' for ECA                  |")
        print("|                                           |")
        print("|        Enter '0' to go back               |")
        print(" -------------------------------------------")

    def personal_data_input(self):
        id = int(input('Student Id: '))
        self.verify = id
        if not self.id_exist(self.userfile):
            raise Exception("Id not found in Database.")

        details = {'Name': None, 'Level': None, 'Section': None, 'Roll no': None, 'Gender': None, 'Phone No: ': None, 'Address': None}
        for i in details.keys():
            if i == 'Gender':
                self.gender_selector_ui()
                choice = input('Your choice: ')
                detail = self.gender_selector(choice)
            else:
                detail = input(f'{i}: ')
            details[i] = detail
        return id, list(details.values())
    
    def marks_data_input(self):
        id = int(input("Student Id: "))
        self.verify = id
        if not self.id_exist(self.userfile):
            raise Exception("Id not found in Database.")
        marks = []
        for i in range(1, 6):
            mark = int(input(f'subject {i}: '))
            if not 0 <= mark <= 100: 
                raise Exception("Please enter valid Marks")
            marks.append(mark)
        return id, marks
    
    def eca_data_input(self):
        id = int(input("Student Id: "))
        self.verify = id
        if not self.id_exist(self.userfile):
            raise Exception("Id not found in database.")
        sports = []
        print('press 0 after completing adding ECA')
        i = 1
        while True:
            sport = input(f'Sport {i}')
            if sport == '0':
                break
            sports.append(sport)
            i += 1
        return id, sports
    
    def write_updated_data(self, passfile, id, datas):
        with open(passfile, 'a') as file:
            file.write(f'{id}:' + ':'.join(map(str, datas)) + '\n')

    def write_modified_data(self, passfile, id, datas):
        with open(passfile, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for i, line in enumerate(lines):
                searched_id = line.split(":")[0]
                if id == int(searched_id):
                    lines[i] = f'{id}:' + ':'.join(map(str, datas)) + '\n'
                    update_success = True
                    break
            if update_success:
                file.seek(0)    
                file.writelines(lines)
            else:
                raise Exception('Failed in Modifying Personal information.')

    def delete_data(self, passfile):
        self.check_file_exist(passfile)
        while True:
            try:
                id = int(input('Student Id: '))
                self.verify = id
                if not self.id_exist(self.userfile):
                    raise Exception("Id not found in Database.")
                with open(passfile, 'r+')as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for line in lines:
                        if id != int(line.split(':')[0]):
                            file.write(line)

                print('✅ Successfully deleted data.')
                choice = input('Do you want to continue deleting(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return
                else:
                    raise Exception('Invalid Choice.')
        
            except ValueError:
                print('\033[31mError! Please enter only number.\033[0m')
            except Exception as e:
                print(f'\033[31mError! {e}\033[0m]')

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
                print('\033[31mError! file not found.\033[0m')
            except PermissionError:
                print('\033[31mError! Premission denied to wirte in this file\033[0m')
            except Exception as e:
                print(f'\033[31m{e}\033[0m')
                
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
        self.check_file_exist(self.userfile)
        while True:
            try:
                name = input('Student Name: ')
                section = input('Section: ')
                clss = int(input('Level :'))
                id = int(input('Id: '))
                verification_id = input('Verification Id: ')
                self.verify = id
                if not self.empty_content(self.userfile):
                    if self.id_exist(self.userfile):
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
        self.check_file_exist(self.personalfile)
        while True:
            try:
                id, details_list = self.personal_data_input()
                self.write_updated_data(self.personalfile, id, details_list)
                choice = input('Do you want to continue Updating(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return
                else:
                    raise Exception('Invalid Choice.')
            
            except ValueError:
                print('\033[31mError! You can only enter number.\033[0m')
            except PermissionError:
                print('\033[31mError! Permission denied to write in this file.\033[0m')
            except Exception as e:
                print(f'\033[31mError! {e}\033[0m')
                
    def update_marks(self):
        self.check_file_exist(self.gradefile)
        while True:
            try: 
                id, marks = self.marks_data_input()
                self.write_updated_data(self.gradefile, id, marks)

                print('✅ Successfully Added student.')
                choice = input('Do you want to continue adding(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    break
                else:
                    print('Invalid Choice')

            except PermissionError:
                print(f"\033[31mError! Permission denied to update marks\033[0m")
            except ValueError:
                print(f"\033[31mError! You can only enter numbers\033[0m")
            except Exception as e:
                print(f"\033[31mError! {e}\033[0m")

    def update_eca(self):
        self.check_file_exist(self.ecafile)
        while True:
            try: 
                id, sports = self.eca_data_input()
                self.write_updated_data(self.ecafile, id, sports)
                print('✅ Successfully Updated ECA record.')
                choice = input('Do you want to continue updating ECA(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return
                else:
                    print('\033[31mInvalid Choice\033[0m')
                    
            except PermissionError:
                print(f"\033[31mError! Permission denied to update marks\033[0m")
            except ValueError:
                print(f"\033[31mError! You can only enter numbers\033[0m")
            except Exception as e:
                print(f"\033[31mError! {e}\033[0m")
    
    def update_record(self):
        self.choices_ui()
        choice = input('Your choice: ')
        if choice == '1':
            self.update_personal()
        elif choice == '2':
            self.update_marks()
        elif choice == '3':
            self.update_eca()
        elif choice == '0':
            return 
        else:
            print('\033[31mInvalid  Choice!\033[0m')
    
    def modify_personal(self):
        self.check_file_exist(self.personalfile)
        while True:
            try:
                id, details_list = self.personal_data_input()
                self.write_modified_data(self.personalfile, id, details_list)
                print('✅ Successfully Personal information Modified.')
                choice = input('Do you want to continue modifying marks(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return
                else:
                    raise Exception("Invalid Choice")
                
            except ValueError:
                print('\033[31mError! You can only enter number.\033[0m')
            except PermissionError:
                print('\033[31mError! Permission denied to write in this file.\033[0m')
            except Exception as e:
                print(f'\033[31mError! {e}\033[0m')

    def modify_marks(self):
        self.check_file_exist(self.personalfile)
        while True:
            try:
                id, marks = self.marks_data_input()
                self.write_modified_data(self.personalfile, id, marks)
                print('✅ Successfully Grade Modified.')
                choice = input('Do you want to continue modifying marks(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return 
                else:
                    raise Exception('Invalid Choice')
                
            except ValueError:
                print('\033[31mError! You can only enter number.\033[0m')
            except PermissionError:
                print('\033[31mError! Permission denied to write in this file.\033[0m')
            except Exception as e:
                print(f'\033[31Error! {e}\033[0m')

    def modify_eca(self):
        self.check_file_exist(self.ecafile)
        while True:
            try: 
                id, sports = self.eca_data_input()
                self.write_modified_data(self.ecafile, id, sports)
                print('✅ Successfully ECA Modified.')
                choice = ('Do you want to continue Modifying ECA(Y/N): ')
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    return
                else:
                    raise Exception('Invalid Choice.')
        
            except ValueError:
                print('\033[31mError! You can only enter number.\033[0m')
            except PermissionError:
                print('\033[31mError! Permission denied to write in this file.\033[0m')
            except Exception as e:
                print(f'\033[31Error! {e}\033[0m')

    def modify_record(self):
        self.choices_ui()
        choice = input('Your Choice: ')
        if choice == '1':
            self.modify_personal()
        elif choice == '2':
            self.modify_marks()
        elif choice == '3':
            self.modify_eca()
        elif choice == '0':
            return
        else:
            print('\033[31mInvalid Choice!\033[0m')

    def delete_personal(self):
        self.delete_data(self.personalfile)

    def delete_marks(self):
        self.delete_data(self.gradefile)

    def delete_eca(self):
        self.delete_data(self.ecafile)

    def delete_record(self):
        self.choices_ui()
        choice = input('Your Choice: ')
        if choice == '1':
            self.delete_personal()
        elif choice == '2':
            self.delete_marks()
        elif choice == '3':
            self.delete_eca()
        elif choice == '0':
            return
        else:
            print('\033[31mInvalid Choice!\033[0m')

    def admin_options(self):
        while True:
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
                print('\033[31mInvalid Choice.\033[0m')

    def mainpage(self):
        while True:
            self.admin_login()
            if self.goback:
                return
            self.admin_options()

class Student(StudentManagementSystem):
    def __init__(self):
        super().__init__()
        self.student_id = None  # Store student ID permanently
        
    def student_ui(self):
        self.clscr()
        print(" =============================================================")
        print("|                        Student page                         |")
        print(" =============================================================")
        print("|                                                             |")
        print("|                      Enter '1' to Update Profile            |")
        print("|                                                             |")
        print("|                      Enter '2' to View Profile              |")
        print("|                                                             |")
        print("|                      Enter '3' to View Grades               |")
        print("|                                                             |")
        print("|                      Enter '4' to View ECA                  |")
        print("|                                                             |")
        print("|                      Enter '0' to Go Back                   |")
        print("|                                                             |")
        print(" =============================================================")

    def update_profile(self):
        try:
            self.check_file_exist(self.personalfile)
            print("\nUpdate Personal Information")
            print("--------------------------")
            
            # Check if profile already exists
            profile_exists = False
            with open(self.personalfile, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    if parts[0] == self.student_id:
                        profile_exists = True
                        break
            
            # Get personal details
            details = {'Name': None, 'Level': None, 'Section': None, 'Roll no': None, 'Gender': None, 'Phone No': None, 'Address': None}
            for i in details.keys():
                if i == 'Gender':
                    self.gender_selector_ui()
                    choice = input('Your choice: ')
                    detail = self.gender_selector(choice)
                else:
                    detail = input(f'{i}: ')
                details[i] = detail
            
            # Write or update profile
            if profile_exists:
                # Update existing profile
                with open(self.personalfile, 'r') as file:
                    lines = file.readlines()
                
                with open(self.personalfile, 'w') as file:
                    for line in lines:
                        if line.split(':')[0] != self.student_id:
                            file.write(line)
                        else:
                            file.write(f"{self.student_id}:" + ':'.join(map(str, details.values())) + '\n')
                print("✅ Profile updated successfully.")
            else:
                # Create new profile
                with open(self.personalfile, 'a') as file:
                    file.write(f"{self.student_id}:" + ':'.join(map(str, details.values())) + '\n')
                print("✅ Profile created successfully.")
            
            self.timer(2)
            
        except Exception as e:
            print(f"\033[31mError! {e}\033[0m")
            self.timer(2)

    def view_profile(self):
        try:
            self.check_file_exist(self.personalfile)
            profile_found = False
            
            # Get student name from user file
            student_name = "Student"
            with open(self.userfile, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    if parts[0] == self.student_id:
                        student_name = parts[1]
                        break
            
            self.clscr()
            print(f"\n{student_name}'s Profile")
            print("=" * 50)
            
            with open(self.personalfile, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    if parts[0] == self.student_id and len(parts) >= 8:
                        profile_found = True
                        
                        # Create data for tabulate
                        fields = ["Id", "Name", "Level", "Section", "Roll No", "Gender", "Phone No", "Address"]
                        values = parts[:8]
                        table_data = [[field, value] for field, value in zip(fields, values)]
                        
                        # Display using tabulate
                        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="fancy_grid"))
                        break
            
            if not profile_found:
                print("\033[31mProfile not found. Please update your profile first.\033[0m")
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\033[31mError! {e}\033[0m")
            self.timer(2)

    def view_marks(self):
        try:
            self.check_file_exist(self.gradefile)
            marks_found = False
            
            self.clscr()
            print("\nYour Academic Performance")
            print("=" * 50)
            
            with open(self.gradefile, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    if parts[0] == self.student_id and len(parts) >= 6:
                        marks_found = True
                        
                        # Get marks from line and convert to int
                        marks = [int(parts[i]) for i in range(1, 6)]
                        
                        # Create subject marks table data
                        subjects = [f"Subject {i}" for i in range(1, 6)]
                        marks_with_total = [f"{mark}/100" for mark in marks]
                        table_data = [[subject, mark] for subject, mark in zip(subjects, marks_with_total)]
                        
                        # Display marks using tabulate
                        print("\nSubject-wise Marks:")
                        print(tabulate(table_data, headers=["Subject", "Marks"], tablefmt="fancy_grid"))
                        
                        # Calculate total and percentage
                        total = sum(marks)
                        percentage = total / 5
                        
                        # Determine grade
                        if percentage >= 90:
                            grade = "A+"
                        elif percentage >= 80:
                            grade = "A"
                        elif percentage >= 70:
                            grade = "B+"
                        elif percentage >= 60:
                            grade = "B"
                        elif percentage >= 50:
                            grade = "C"
                        else:
                            grade = "F"
                        
                        # Create summary table data
                        summary_data = [
                            ["Total Marks", f"{total}/500"],
                            ["Percentage", f"{percentage:.2f}%"],
                            ["Grade", grade]
                        ]
                        
                        # Display summary using tabulate
                        print("\nSummary:")
                        print(tabulate(summary_data, headers=["Parameter", "Value"], tablefmt="fancy_grid"))
                        break
            
            if not marks_found:
                print("\033[31mNo grade records found.\033[0m")
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\033[31mError! {e}\033[0m")
            self.timer(2)

    def view_eca(self):
        try:
            self.check_file_exist(self.ecafile)
            eca_found = False
            
            self.clscr()
            print("\nYour Extra-Curricular Activities")
            print("=" * 50)
            
            with open(self.ecafile, 'r') as file:
                for line in file:
                    parts = line.strip().split(":")
                    if parts[0] == self.student_id and len(parts) > 1:
                        eca_found = True
                        # Get activities excluding id
                        activities = parts[1:]
                        
                        # Filter out empty activities
                        activities = [activity for activity in activities if activity.strip()]
                        
                        if activities:
                            # Create table data for activities
                            table_data = [[i, activity] for i, activity in enumerate(activities, 1)]
                            
                            # Display using tabulate
                            print(tabulate(table_data, headers=["No.", "Activity"], tablefmt="fancy_grid"))
                        else:
                            print("\033[31mNo activities found in your ECA record.\033[0m")
                        break
            
            if not eca_found:
                print("\033[31mNo ECA records found.\033[0m")
            
            input("\nPress Enter to continue...")
            
        except Exception as e:
            print(f"\033[31mError! {e}\033[0m")
            self.timer(2)

    def student_sign_up(self, passfile):
        try:
            with open(passfile, 'r') as file:
                pass
        except FileNotFoundError:
            with open(passfile, 'w') as file:
                pass
        while True:
            try:
                self.username = input('Username: ')
                if len(self.username) < 3:
                    raise Exception ("\033[31mError! Username must be at least more than 2 character\033[0m")
                
                # Check if username already exists
                if not self.empty_content(passfile) and self.check_username_exist(passfile):
                    raise Exception("\033[31mError! Username already exists. Please choose another username.\033[0m")
                    
                self.password = input('Password: ')
                if len(self.password) < 5: 
                    raise Exception ("\033[31mError! Password must be more than 4 character.\033[0m")
                if not any(char.isalpha() for char in self.password) or not any(char.isdigit() for char in self.password):
                    raise Exception ("\033[31mError! Password must consist alphabet and numbers.\033[0m")
                id = input('verification Id: ')
                self.verify = id
                if not self.check_verification():
                    raise Exception ("\033[31mError! Verification id didn't match.\033[0m")
                
                # Get student ID from verification record
                student_id = None
                with open(self.cfm_student, 'r') as vfile:
                    for line in vfile:
                        v_id, v_name, v_class, v_section, v_verify = line.strip().split(":")
                        if v_verify == self.verify:
                            student_id = v_id
                            break
                
                if not student_id:
                    raise Exception("\033[31mError! Unable to retrieve student ID.\033[0m")
                    
                with open(passfile, 'a') as file:
                    file.write(f"{student_id}:{self.username}:{self.password}\n")
                    print("✅ Sign up succesfull.")
                    self.timer(2)

                return
            
            except PermissionError: 
                print(f'Error! Permission denied to write in file')
                choice = input("Try again? (Y/N): ")
                if choice.lower() != 'y':
                    self.goback = True
                    return
            except Exception as e:
                print(f"{e}")
                choice = input("Try again? (Y/N): ")
                if choice.lower() != 'y':
                    self.goback = True
                    return

    def student_login(self):
        self.login_ui(2)
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.sign_in(self.studentfile)
                # Store the student ID permanently after successful login
                if not self.goback:
                    self.student_id = self.verify
                return
            elif choice == '2':
                self.student_sign_up(self.studentfile)
                return
            elif choice == '0':
                self.goback = True
                return
            else:
                print('Invalid Choice!')
    
    def student_options(self):
        while True:
            self.student_ui()
            choice = input('Your choice: ')
            if choice == '1':
                self.update_profile()
            elif choice == '2':
                self.view_profile()
            elif choice == '3':
                self.view_marks()
            elif choice == '4':
                self.view_eca()
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
            self.student_options()
            if self.goback:
                return

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