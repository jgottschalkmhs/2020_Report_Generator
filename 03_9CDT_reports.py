import csv

# Function goes here


# Converts text file into a list
def make_list(file_name):
    list_name = open(file_name).read().splitlines()
    return list_name


# Main Routine starts here

data = []

# Open File
student_list = open("9CDT_B_data.csv")

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
        him = "him"
    else:
        he = "she"
        He = "She"
        his = "her"
        himself = "herself"
        him = "her"

    if classwork == "1":
        progress = "limited"
        completes_work = "struggled to complete the coursework"
    elif classwork == "2":
        progress = "some"
        completes_work = "completed some of the coursework to an acceptable standard"
    elif classwork == "3":
        progress = "steady"
        completes_work = "attempted to complete most of the coursework and generally did so to a high standard"
    else:
        progress = "outstanding"
        completes_work = "always completed the set work to a high standard"

    if effort == "1":
        advice = "{} is welcome to take 10CDT next year but {} would need to be prepared to work hard and " \
                 "focus on the task at hand.".format(first_name, he)
    elif effort == "2":
        advice = "{} is welcome to take 10CDT next year.  If {} chooses to do that course {} would need to " \
                 "strive to complete all of the coursework before the deadline.".format(first_name, he, he)
    elif effort == "3":
        advice = "I'd encourage {} to take 10CDT next year and would advise {} to ask for help when necessary and " \
                 "aim to create more sophisticated outcomes.".format(first_name, him)
    else:
        advice = "I'd encourage {} to take 10CDT next year as {} has a talent for this subject, and I suspect " \
                 "{} would really enjoy taking {} work to the next level.".format(first_name, he, he, his)

    first_line = "{} is {} student who has made {} progress in this course.".format(first_name, adjective, progress)
    second_line = "In class, {} {}.".format(first_name, completes_work)
    third_line = advice

    print()
    print("{} {} {}".format(first_line, second_line, third_line))
