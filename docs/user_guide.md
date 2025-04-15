# Student Management System - User Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Admin Guide](#admin-guide)
5. [Student Guide](#student-guide)
6. [Troubleshooting](#troubleshooting)

## Introduction

The Student Management System is a console-based application designed to manage student records, academic information, and extracurricular activities. This guide provides step-by-step instructions for both administrators and students on how to use the system effectively.

## Installation

### System Requirements

- Python 3.x
- Required Python packages (install via pip):
  - cryptography
  - tabulate

### Installation Steps

1. Clone or download the Student Management System files to your local machine.
2. Open a terminal/command prompt and navigate to the project directory.
3. Install required packages:

```bash
pip install cryptography tabulate
```

4. Run the application:

```bash
python main.py
```

## Getting Started

Upon starting the application, you will see the main interface:

```
 =============================================================
|                   Student Management System                 |
 =============================================================
|                                                             |
|                   Enter '1' for Admin login                 |
|                                                             |
|                  Enter '2' for Student login                |
|                                                             |
 =============================================================
```

- Enter `1` to access the Admin interface
- Enter `2` to access the Student interface

## Admin Guide

### Admin Login/Registration

1. From the main menu, select option `1` for Admin login.
2. You will see the Admin login screen:

```
 =============================================================
|                    Admin Login page                         |
 =============================================================
|                                                             |
|                      Enter '1' to Sign In                   |
|                                                             |
|                      Enter '2' to Sign Up                   |
|                                                             |
|                      Enter '0' to Go Back                   |
|                                                             |
 =============================================================
```

3. Select option `1` to sign in with existing credentials or `2` to create a new admin account.

#### Admin Sign Up

If you select option `2` to sign up:

1. Enter a username (must be at least 3 characters)
2. Enter a password (must be at least 5 characters and contain both letters and numbers)
3. After successful registration, you will be redirected to the admin dashboard.

#### Admin Sign In

If you select option `1` to sign in:

1. Enter your username
2. Enter your password
3. After successful authentication, you will be redirected to the admin dashboard.

### Admin Dashboard

After successful login, you will see the admin dashboard:

```
 =============================================================
|                          Admin page                         |
 =============================================================
|                                                             |
|                      Enter '1' to Add Student               |
|                                                             |
|                      Enter '2' to Update Record             |
|                                                             |
|                      Enter '3' to Modify Record             |
|                                                             |
|                      Enter '4' to Delete Record             |
|                                                             |
|                      Enter '0' to Go Back                   |
|                                                             |
 =============================================================
```

### Adding a Student

To add a new student:

1. Select option `1` from the admin dashboard.
2. Enter the student's details:
   - Student Name
   - Section
   - Level (class)
   - ID
   - Verification ID (this will be used by the student during registration)
3. The system will confirm successful addition of the student.
4. You can choose to add more students or return to the dashboard.

### Updating Student Records

To add new information to a student's record:

1. Select option `2` from the admin dashboard.
2. You will see the following menu:

```
 -------------------------------------------
|                 RECORDS                   |
|                                           |
|        Enter '1' for personal info        |
|                                           |
|        Enter '2' for Grades               |
|                                           |
|        Enter '3' for ECA                  |
|                                           |
|        Enter '0' to go back               |
 -------------------------------------------
```

3. Select the type of information you want to update:

#### Updating Personal Information

1. Select option `1` to update personal information.
2. Enter the student's ID.
3. Enter the student's personal details:
   - Name
   - Level
   - Section
   - Roll No
   - Gender (select from options)
   - Phone Number
   - Address
4. The system will confirm successful update.

#### Updating Grades

1. Select option `2` to update grades.
2. Enter the student's ID.
3. Enter marks for 5 subjects (values between 0-100).
4. The system will confirm successful update.

#### Updating Extracurricular Activities

1. Select option `3` to update ECA.
2. Enter the student's ID.
3. Enter the student's activities one by one.
4. Enter `0` when you've finished adding activities.
5. The system will confirm successful update.

### Modifying Student Records

To modify existing records:

1. Select option `3` from the admin dashboard.
2. You will see the records menu as shown in the "Updating Student Records" section.
3. Select the type of information you want to modify.
4. Enter the student's ID and the new information.
5. The system will update the existing record with the new information.

### Deleting Student Records

To delete student records:

1. Select option `4` from the admin dashboard.
2. You will see the records menu as shown in the "Updating Student Records" section.
3. Select the type of information you want to delete.
4. Enter the student's ID.
5. The system will delete the specified record.

## Student Guide

### Student Login/Registration

1. From the main menu, select option `2` for Student login.
2. You will see the Student login screen:

```
 =============================================================
|                      Student Login Page                     |
 =============================================================
|                                                             |
|                      Enter '1' to Sign In                   |
|                                                             |
|                      Enter '2' to Sign Up                   |
|                                                             |
|                      Enter '0' to Go Back                   |
|                                                             |
 =============================================================
```

3. Select option `1` to sign in with existing credentials or `2` to register as a new student.

#### Student Sign Up

If you select option `2` to sign up:

1. Enter a username (must be at least 3 characters)
2. Enter a password (must be at least 5 characters and contain both letters and numbers)
3. Enter the verification ID provided by your administrator
4. After successful registration, you will be redirected to the student dashboard.

#### Student Sign In

If you select option `1` to sign in:

1. Enter your username
2. Enter your password
3. After successful authentication, you will be redirected to the student dashboard.

### Student Dashboard

After successful login, you will see the student dashboard:

```
 =============================================================
|                        Student page                         |
 =============================================================
|                                                             |
|                      Enter '1' to Update Profile            |
|                                                             |
|                      Enter '2' to View Profile              |
|                                                             |
|                      Enter '3' to View Grades               |
|                                                             |
|                      Enter '4' to View ECA                  |
|                                                             |
|                      Enter '0' to Go Back                   |
|                                                             |
 =============================================================
```

### Updating Profile

To update your personal information:

1. Select option `1` from the student dashboard.
2. Enter your personal details:
   - Name
   - Level
   - Section
   - Roll No
   - Gender (select from options)
   - Phone Number
   - Address
3. The system will confirm successful update.

### Viewing Profile

To view your profile information:

1. Select option `2` from the student dashboard.
2. The system will display your personal information in a formatted table.

### Viewing Grades

To view your academic performance:

1. Select option `3` from the student dashboard.
2. The system will display:
   - Subject-wise marks
   - Total marks
   - Percentage
   - Grade

### Viewing Extracurricular Activities

To view your extracurricular activities:

1. Select option `4` from the student dashboard.
2. The system will display all your registered activities.

## Troubleshooting

### Common Issues and Solutions

1. **Unable to Log In**:
   - Verify that you are using the correct username and password.
   - Ensure that caps lock is not enabled.
   - If you've forgotten your credentials, contact the system administrator.

2. **Student Unable to Register**:
   - Confirm that you are using the correct verification ID provided by your administrator.
   - Ensure that your username is not already taken.
   - Make sure your password meets the requirements.

3. **File-Related Errors**:
   - Ensure that the application has permission to read/write to the directory.
   - If files are corrupted, the administrator may need to reset the affected data files.

4. **Display Issues**:
   - If tables are not displaying correctly, ensure you have the tabulate package installed.
   - Adjust your console window size if tables appear truncated.

### Contacting Support

If you encounter persistent issues that are not addressed in this guide, please contact your system administrator or technical support team. 