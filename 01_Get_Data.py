import csv

# Function goes here

# Converts text file into a list
def make_list(file_name):
    list_name = open(file_name).read().splitlines()
    return list_name


# Main Routine starts here

data = []

# Open File
student_list = open("9KVS_data.csv")

# Read data into list
students = csv.reader(student_list)

for row in students:
    data.append(row)

print(data)
