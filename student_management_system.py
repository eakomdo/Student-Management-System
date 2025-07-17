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
student_directory = {
    'student no.1': {'name': 'Mike', 'age': 12, 'subject': 'Maths', 'grade': 76.0}
}


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