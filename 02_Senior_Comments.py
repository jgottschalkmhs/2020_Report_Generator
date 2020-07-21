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

for item in data:
    first_name = item[0]
    gender = item[1]
    effort = item[2]
    classwork = item[3]
    adjective = item[4]

    if gender == "M":
        he = "he"
        He = "He"
        his = "his"
        himself = "himself"
    else:
        he = "she"
        He = "She"
        his = "her"
        himself = "herself"

    if classwork == "1":
        progress = "limited"
        completes_work = "struggles to complete the work that has been set"
    elif classwork == "2":
        progress = "some"
        completes_work = "sometimes completes the set work to an acceptable standard"
    elif classwork == "3":
        progress = "steady"
        completes_work = "usually completes the set work to a high standard"
    else:
        progress = "outstanding"
        completes_work = "always completes the set work to a high standard"

    if effort == "1":
        advice = "focus in class and ask for help when necessary"
    elif effort == "2":
        advice = "avoid becoming distracted and strive to complete all of the coursework before the deadline"
    elif effort == "3":
        advice = "ask for help when necessary and aim to create more sophisticated outcomes"
    else:
        advice = "continue to strive for Excellence and think about creative ways to take their work to the next level"

    first_line = "{} is {} student who has made {} progress in this course.".format(first_name, adjective, progress)
    second_line = "In class, {} {}.".format(first_name, completes_work)
    third_line = "Going forward I'd urge {} to {}.".format(first_name, advice)

    print()
    print("{} {} {}".format(first_line, second_line, third_line))
