# Student Details
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
middle_initial = input("Enter Middle Initial: ")
course = input("Enter Course: ")
year_level = input("Enter Year Level: ")

# Login Details
username = 'PSU Admin'
password = 'System08'

# Check username and password
if input("Enter username: ") != username or input("Enter password: ") != password:
    print("Invalid Login Details. Access Denied.")
    exit()

# Data Science Program Subjects
subjects_dict = {
    "Dictionary 1": {
        "Year Level": "First Year",
        "GE Courses": "Envi Scie, Algebra",
        "Professional Course": "Eng1, Fil1, PE1",
        "Core Course": "CC1, CC2",
        "Miscellaneous and Devt Fee": 2000
    },
    "Dictionary 2": {
        "Year Level": "Second Year",
        "GE Courses": "Cal2, Linear, Physics 1",
        "Professional Course": "Eng3, Fil1, PE3",
        "Core Course": "CC4, CC5",
        "Miscellaneous and Devt Fee": 2500
    },
    "Dictionary 3": {
        "Year Level": "Third Year",
        "GE Courses": "Pol Sci Anthro1, Psych1",
        "Professional Course": "Writing1, DataSci1",
        "Core Course": "CC6, CC10, Thesis1",
        "Miscellaneous and Devt Fee": 3000
    },
    "Dictionary 4": {
        "Year Level": "Fourth Year",
        "GE Courses": "Acctg1, Rizal",
        "Professional Course": "Writing 3, Data Sci3",
        "Core Course": "Elect1, Elect2, Thesis2",
        "Miscellaneous and Devt Fee": 3500
    }
}

# Compute Functions
def payment_model1(tuition, discount):
    return (tuition - (tuition * discount))

def payment_model2(tuition, discount, num_installments):
    installment_amount = tuition / num_installments
    total_payment = (tuition - (tuition * discount)) + ((num_installments - 1) * installment_amount)
    return installment_amount, total_payment

def payment_model3(tuition, partial_payment):
    balance = tuition - partial_payment
    return balance

# Tuition Calculation
tuition_per_unit = 1000
num_subjects = 3
misc_devt_fee = subjects_dict[f"Dictionary {year_level}"]["Miscellaneous and Devt Fee"]
units = num_subjects * 3
tuition = (tuition_per_unit * units) - 0  # 0 discount for now

# Payment Mode Selection
print("Select Payment Mode:")
print("1. Full Payment (5% Discount)")
print("2. Two Installments (3% Discount)")
print("3. Partial Payment (No Discount)")
payment_mode = input("Enter Payment Mode: ")

if payment_mode == "1":
    tuition = payment_model1(tuition, 0.05)
elif payment_mode == "2":
    num_installments = 2
    installment_amount, total_payment = payment_model2(tuition, 0.03, num_installments)
elif payment_mode == "3":
    partial_payment = int(input("Enter Partial Payment: "))
    balance = payment_model3(tuition, partial_payment)
else:
    print("Invalid Payment Mode. Please try")
