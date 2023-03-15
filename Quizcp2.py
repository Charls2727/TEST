# Create dictionaries for each subject
first_year = {
    'Year Level': 'First Year',
    'GE Courses': ['Envi Scie', 'Algebra'],
    'Professional Course': ['Eng1', 'Fil1', 'PE1'],
    'Core Course': ['CC1', 'CC2'],
    'Miscellaneous and Devt Fee': 2000
}

second_year = {
    'Year Level': 'Second Year',
    'GE Courses': ['Cal2', 'Linear', 'Physics 1'],
    'Professional Course': ['Eng3', 'Fil1', 'PE3'],
    'Core Course': ['CC4', 'CC5'],
    'Miscellaneous and Devt Fee': 2500
}

third_year = {
    'Year Level': 'Third Year',
    'GE Courses': ['Pol Sci', 'Anthro1', 'Psych1'],
    'Professional Course': ['Writing1', 'DataSci1'],
    'Core Course': ['CC6', 'CC10', 'Thesis1'],
    'Miscellaneous and Devt Fee': 3000
}

fourth_year = {
    'Year Level': 'Fourth Year',
    'GE Courses': ['Acctg1', 'Rizal'],
    'Professional Course': ['Writing3', 'DataSci3'],
    'Core Course': ['Elect1', 'Elect2', 'Thesis2'],
    'Miscellaneous and Devt Fee': 3500
}

# Function to calculate tuition fee
def complete():
    # Ask user for inputs
    year_level = input("Enter Year Level: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    middle_initial = input("Enter Middle Initial: ")
    
    # Select the corresponding dictionary based on year level input
    if year_level == 'First Year':
        subject_dict = first_year
    elif year_level == 'Second Year':
        subject_dict = second_year
    elif year_level == 'Third Year':
        subject_dict = third_year
    elif year_level == 'Fourth Year':
        subject_dict = fourth_year
    else:
        print("Invalid Year Level")
        return
    
    # Calculate total units
    num_subjects = len(subject_dict['GE Courses']) + len(subject_dict['Professional Course']) + len(subject_dict['Core Course'])
    total_units = num_subjects * 3
    
    # Calculate tuition fee
    tuition_fee = total_units * 1000 + subject_dict['Miscellaneous and Devt Fee']
    
    # Print student information and tuition fee
    print(f"Name: {last_name}, {first_name} {middle_initial}.")
    print(f"Year Level: {year_level}")
    print(f"Total Units: {total_units}")
    print(f"Tuition Fee: {tuition_fee}")
