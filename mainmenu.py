def main_menu():
    print("Main Menu:")
    print("1. Add a new employee")
    print("2. Delete an employee")
    print("3. Update an employee's information")
    print("4. Generate a report")
    print("5. Exit the program")
    option = int(input("Enter your choice: "))
    return option

# Example usage:
while True:
    choice = main_menu()
    if choice == 1:
        # Call function to add a new employee
        print("Adding a new employee...")
    elif choice == 2:
        # Call function to delete an employee
        print("Deleting an employee...")
    elif choice == 3:
        # Call function to update an employee's information
        print("Updating an employee's information...")
    elif choice == 4:
        # Call function to generate a report
        print("Generating a report...")
    elif choice == 5:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
