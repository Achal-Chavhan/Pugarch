# Day 01 - Python Practice

This folder contains the Python programs I completed as part of Day 01 practice.

The work is divided into two parts:

1. **Exercises** - 15 basic Python programming problems
2. **Employee Management** - A command-line employee management application

## Folder Structure

```text
day-01/
│
├── exercises_d1.py
├── employee-management.py
└── README.md
```

## 1. Python Exercises

The `exercises_d1.py` file contains 15 programming problems covering basic Python concepts such as strings, lists, loops, conditions, functions, and arrays.

The problems included are:

1. Reverse a string
2. Check whether a string is a palindrome
3. Find the largest number in a list
4. Find the second largest number
5. Remove duplicate elements from a list
6. Find a missing number
7. Find duplicate numbers
8. Count character frequency in a string
9. Find the first non-repeating character
10. Merge two sorted arrays
11. Find common elements in two lists
12. Implement a stack
13. Implement a queue
14. Find the maximum subarray sum
15. Sort a list without using built-in sorting

These exercises helped me practice basic problem-solving and understand how different Python concepts work together. The file includes the requested 15 problems, from string reversal through sorting.

### How to Run

Open a terminal in the project folder and run:

```bash
python exercises_d1.py
```

Some programs take input from the user, while others use sample lists directly in the program.



## 2. Employee Management CLI

The `employee-management.py` file is a simple command-line Employee Management System.

It allows the user to manage employee information using a menu-based interface.

### Features

The application provides the following options:

* **Add Employee** - Add a new employee with ID, name, department, and salary.
* **Update Employee** - Update an existing employee's details.
* **Delete Employee** - Remove an employee using their ID.
* **Search Employee** - Search for an employee by ID.
* **List Employees** - Display all employees.
* **Highest Salary** - Find the employee with the highest salary.
* **Average Salary** - Calculate the average salary of all employees.
* **Department Filter** - Display employees belonging to a particular department.
* **Exit** - Close the application.

The main menu provides all nine options directly through the command line.

### Employee Information

Each employee is stored with:

```text
Employee ID
Name
Department
Salary
```

The program keeps the employee records in a list and stores each employee's information as a dictionary.

### Salary Features

The application can find the employee with the highest salary and calculate the average salary of all employees.

### How to Run

Run the following command:

```bash
python employee-management.py
```

The program will display a menu like this:

```text
==============================
   EMPLOYEE MANAGEMENT SYSTEM
==============================
1. Add Employee
2. Update Employee
3. Delete Employee
4. Search Employee
5. List Employees
6. Highest Salary
7. Average Salary
8. Department Filter
9. Exit

Enter your choice:
```

## Concepts Used

Through these programs, I practiced:

* Variables
* Strings
* Lists
* Dictionaries
* `if` and `else`
* `for` loops
* `while` loops
* Functions
* Searching
* Sorting
* Basic data handling
* Command-line input and output

## Conclusion

This Day 01 practice helped me improve my understanding of basic Python programming and problem-solving. The exercises focus on small programming problems, while the Employee Management project combines these concepts into a simple practical application.
