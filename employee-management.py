employees = []


# Add Employee
def add_employee():
    print("\n--- Add Employee ---")

    emp_id = input("Enter Employee ID: ").strip()
    if not emp_id:
        print("Employee ID cannot be empty!")
        return

    # Check if ID already exists
    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()

    try:
        salary = float(input("Enter Salary: "))
        if salary < 0:
            print("Salary cannot be negative!")
            return
    except ValueError:
        print("Invalid salary! Please enter a valid number.")
        return

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully!")


# Update Employee
def update_employee():
    print("\n--- Update Employee ---")

    emp_id = input("Enter Employee ID: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            print("(Press Enter to keep current value)")

            new_name = input(f"Enter new name [{employee['name']}]: ").strip()
            if new_name:
                employee["name"] = new_name

            new_department = input(f"Enter new department [{employee['department']}]: ").strip()
            if new_department:
                employee["department"] = new_department

            new_salary_str = input(f"Enter new salary [{employee['salary']}]: ").strip()
            if new_salary_str:
                try:
                    new_salary = float(new_salary_str)
                    if new_salary >= 0:
                        employee["salary"] = new_salary
                    else:
                        print("Salary cannot be negative. Keeping previous value.")
                except ValueError:
                    print("Invalid number. Keeping previous salary.")

            print("Employee updated successfully!")
            return

    print("Employee not found!")


# Delete Employee
def delete_employee():
    print("\n--- Delete Employee ---")

    emp_id = input("Enter Employee ID: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")


# Search Employee
def search_employee():
    print("\n--- Search Employee ---")

    emp_id = input("Enter Employee ID: ").strip()

    for employee in employees:
        if employee["id"] == emp_id:
            print("\nEmployee Found")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print(f"Salary: ${employee['salary']:,.2f}")
            return

    print("Employee not found!")


# List Employees
def list_employees():
    print("\n--- All Employees ---")

    if len(employees) == 0:
        print("No employees found!")
        return

    for employee in employees:
        print("--------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Department:", employee["department"])
        print(f"Salary: ${employee['salary']:,.2f}")


# Highest Salary
def highest_salary():
    print("\n--- Highest Salary ---")

    if len(employees) == 0:
        print("No employees found!")
        return

    highest = employees[0]

    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    print("Employee:", highest["name"])
    print("Department:", highest["department"])
    print(f"Salary: ${highest['salary']:,.2f}")


# Average Salary
def average_salary():
    print("\n--- Average Salary ---")

    if len(employees) == 0:
        print("No employees found!")
        return

    total = 0
    for employee in employees:
        total = total + employee["salary"]

    average = total / len(employees)
    print(f"Average Salary: ${average:,.2f}")


# Department Filter
def department_filter():
    print("\n--- Department Filter ---")

    department = input("Enter Department: ").strip()

    found = False

    for employee in employees:
        if employee["department"].lower() == department.lower():
            print("--------------------")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print(f"Salary: ${employee['salary']:,.2f}")
            found = True

    if not found:
        print("No employees found in this department.")


# Main Menu
while True:
    print("\n==============================")
    print("   EMPLOYEE MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. List Employees")
    print("6. Highest Salary")
    print("7. Average Salary")
    print("8. Department Filter")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        list_employees()
    elif choice == "6":
        highest_salary()
    elif choice == "7":
        average_salary()
    elif choice == "8":
        department_filter()
    elif choice == "9":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")