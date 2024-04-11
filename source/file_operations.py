"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees(file_path):
    file_path = "employees_list.txt"
   
    employees = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                employee_data = line.strip().split(',')
                employee = {
                    'id': employee_data[0],  
                    'name': employee_data[1],
                    'age': employee_data[2],
                    'position': employee_data[3]
                }
                employees.append(employee)
    except FileNotFoundError:
        print("File not found at the specified path:", file_path)
    
    return employees

file_path = 'employees_list.txt' 
employees_data = read_employees(file_path)
print(employees_data)

  

def write_employees():
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
