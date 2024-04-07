def list_of_departments(employee_data: list):
    departments = set()
    for employee in employee_data:
        departments.add(employee['department'])
    print("List of departments:")
    for department in sorted(departments):
        print(department)


def list_all_employees(employee_data: list):
    print("List of all employees:")
    for employee in employee_data:
        print(f"ID: {employee['ID']}, Name: {employee['first_name']} {employee['last_name']}")


def average_age_and_salary_department(employee_data: list):
    department_data = {}
    for employee in employee_data:
        department = employee['department']
        if department not in department_data:
            department_data[department] = {'total_age': 0, 'total_salary': 0, 'num_employees': 0}
        department_data[department]['total_age'] += int(employee['date_of_birth'][:4])
        department_data[department]['total_salary'] += employee['salary']
        department_data[department]['num_employees'] += 1

    print("Average age and salary per department:")
    for department, data in department_data.items():
        average_age = data['total_age'] / data['num_employees']
        average_salary = data['total_salary'] / data['num_employees']
        print(f"Department: {department}, Average Age: {average_age:.2f}, Average Salary: {average_salary:.2f}")


def employees_in_department(employee_data: list):
    department_employees = {}
    for employee in employee_data:
        department = employee['department']
        if department not in department_employees:
            department_employees[department] = []
        department_employees[department].append(employee)

    print("Employees in each department:")
    for department, employees in department_employees.items():
        print(f"Department: {department}")
        for employee in employees:
            print(f"ID: {employee['ID']}, Name: {employee['first_name']} {employee['last_name']}")
        print()  # Empty line for separation


if _name_ == "_main_":
    EMPLOYEE_DATA = [
        {'ID': 1, 'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': '1990-01-01', 'department': 'HR',
         'salary': 50000}
    ]
    EMPLOYEE_ID = len(EMPLOYEE_DATA) + 1

    while True:
        option = main_menu()
        if option == 1:
            add_employee(EMPLOYEE_DATA, EMPLOYEE_ID)
            EMPLOYEE_ID += 1  # Increment employee ID for the next employee
        elif option == 2:
            delete_employee(EMPLOYEE_DATA, int(input("Enter employee ID: ")))
        elif option == 3:
            update_employee(EMPLOYEE_DATA, int(input("Enter employee ID: ")))
        elif option == 4:
            print("Reports:")
            print("1. List of departments")
            print("2. List of all employees")
            print("3. Average age and salary per department")
            print("4. Employees in each department")
            report_option = int(input("Enter your choice: "))
            if report_option == 1:
                list_of_departments(EMPLOYEE_DATA)
            elif report_option == 2:
                list_all_employees(EMPLOYEE_DATA)
            elif report_option == 3:
                average_age_and_salary_department(EMPLOYEE_DATA)
            elif report_option == 4:
                employees_in_department(EMPLOYEE_DATA)
        elif option == 5:
            break
        else:
            print("Invalid option. Please select again.")