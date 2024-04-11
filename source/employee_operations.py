"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
    # Ask for employee details
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")
    
    # Create a dictionary to store the details
    new_employee = {
        'name': name,
        'age': age,
        'position': position
    }
    
    # Add the new employee to the list of employees
    employees.append(new_employee)
    print("Employee added successfully!")

# Example usage:

add_employee()

def delete_employee():
    # to delete
    employee_id = input("Enter the ID of the employee to delete: ")

    # Check if the employee ID exists
    for employee in employees:
        if employee.get('id') == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return

    # If the ID does not exist
    print("Employee with ID '{}' not found.".format(employee_id))


# Example usage:
employees = [{'id': '1', 'name': 'John', 'age': '30', 'position': 'Manager'},
             {'id': '2', 'name': 'Alice', 'age': '25', 'position': 'Assistant'}]
delete_employee(employees)


def update_employee(employee_data: list, employee_id: int):
    for employee in employee_data:
        if employee['ID'] == employee_id:
            print("Update employee information:")
            employee['first_name'] = input("Enter first name: ")
            employee['last_name'] = input("Enter last name: ")
            employee['date_of_birth'] = input("Enter date of birth (YYYY-MM-DD): ")
            employee['department'] = input("Enter department: ")
            employee['salary'] = float(input("Enter salary: "))
            print(f"Employee with ID {employee_id} updated successfully!")
            return
    print(f"Employee with ID {employee_id} not found.")

# Example usage:
employees = [
    {'ID': 1, 'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': '1990-01-01', 'department': 'HR', 'salary': 50000},
    {'ID': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'date_of_birth': '1985-05-15', 'department': 'IT', 'salary': 60000},
    # More employee data...
]

employee_id_to_update = int(input("Enter the ID of the employee you want to update: "))
update_employee(employees, employee_id_to_update)
