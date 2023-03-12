def compute_tuition():
    # Ask for user input
    year_level = input("Enter your year level: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    middle_initial = input("Enter your middle initial: ")
    num_subjects = int(input("Enter the number of subjects you are taking: "))

    # Compute total number of units
    total_units = num_subjects * 3

    # Compute tuition fee
    tuition_fee = total_units * 1000

    # Add miscellaneous fee
    tuition_fee += 2000

    # Print results
    print("Student Name:", last_name + ",", first_name, middle_initial + ".")
    print("Year Level:", year_level)
    print("Total Units:", total_units)
    print("Tuition Fee: PHP", tuition_fee)

# Call the function
compute_tuition()
