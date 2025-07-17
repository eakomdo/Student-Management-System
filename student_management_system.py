# Collect a student's name, age, subject and grade, then print a message
# Calculate the average grade and determine if the student has passed or failed.
# Display a profile of the student
# Do and eligibity check if a student who is 14+ qualify for a scholarship
#store the data in a dictionary
# options to perform these Actions


'''
    store student data in a dictionary ✅
    give the user options to choose from to perform an action
    make inputs to activate an action
    display student data from the dictionary
    Add student details to the system
    calculate average grades of students
    check eligibility for scholaship
'''
#Initialized our dictionary
student_directory = {}


print(" Welcome to Lavender Sudent Management System")




#adding students
name = input("Enter student name: ")
age = int(input("Enter your age: "))
subject = input("Enter subject: ")
grade = float(input("Enter your grade: "))


#Create a student profile dictionary with the data you have collected

student_profile = {
    "name" : name,
    "age": age,
    "subject": subject,
    "grade": grade
}

student_key = f"student no.{len(student_directory) +1}"

print(student_key)

student_directory[student_key] = student_profile
print(student_directory)

# Displaying the student profile
print(f"\nStudent Profile:\nName: {student_profile['name']}\nAge: {student_profile['age']}\nSubject: {student_profile['subject']}\nGrade: {student_profile['grade']:.2f}")

#Adding a new student profile to the directory

if input("Do you want to add another student? (yes/no): ").strip().lower() == 'yes':
    name = input("Enter student name: ")
    age = int(input("Enter your age: "))
    subject = input("Enter subject: ")
    grade = float(input("Enter your grade: "))

    student_profile = {
        "name": name,
        "age": age,
        "subject": subject,
        "grade": grade
    }

    student_key = f"student no.{len(student_directory) + 1}"
    student_directory[student_key] = student_profile
    print(f"\nNew Student Profile Added:\n{student_profile}")
