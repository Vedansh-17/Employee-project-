def read_employees(file_path):
    file_path = "employees_list.txt"
    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Parameters:
    file_path (str): The path to the text file containing employee data.

    Returns:
    list: A list containing employee data read from the text file.
    """
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
