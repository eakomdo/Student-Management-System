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

#Adding new student profiles to the directory

# First additional student
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
    print(f"\nNew Student Profile Added:\n{student_directory}")
    
    # Second additional student
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
        print(f"\nNew Student Profile Added:\n{student_directory}")
        
        # Third additional student
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
            print(f"\nNew Student Profile Added:\n{student_directory}")
            
            # Fourth additional student
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
                print(f"\nNew Student Profile Added:\n{student_directory}")
                
                # Fifth additional student
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
                    print(f"\nNew Student Profile Added:\n{student_directory}")

# Calculate average grades and check scholarship eligibility
print("\n" + "="*50)
if input("Do you want to calculate average grades? (yes/no): ").strip().lower() == 'yes':
    if student_directory:
        total_grade = sum(student['grade'] for student in student_directory.values())
        average_grade = total_grade / len(student_directory)

        if average_grade >= 50:
            print(f"Average Grade: {average_grade:.2f} - Status: Passed")
        else:
            print(f"Average Grade: {average_grade:.2f} - Status: Failed")
    else:
        print("No students in the directory to calculate average.")

# Check scholarship eligibility
print("\n" + "="*50)
if input("Do you want to check scholarship eligibility? (yes/no): ").strip().lower() == 'yes':
    eligible_students = []
    for student_id, student_info in student_directory.items():
        if student_info['age'] >= 14 and student_info['grade'] >= 70:
            eligible_students.append(f"{student_info['name']} (Age: {student_info['age']}, Grade: {student_info['grade']})")
    
    if eligible_students:
        print("\nScholarship Eligible Students (Age 14+ and Grade 70+):")
        for student in eligible_students:
            print(f"- {student}")
    else:
        print("No students are eligible for scholarship (requirements: Age 14+ and Grade 70+)")

# Display all students
print("\n" + "="*50)
if input("Do you want to display all students? (yes/no): ").strip().lower() == 'yes':
    if student_directory:
        print("\nAll Students in the System:")
        for student_id, student_info in student_directory.items():
            status = "PASSED" if student_info['grade'] >= 50 else "FAILED"
            print(f"\n{student_id}:")
            print(f"  Name: {student_info['name']}")
            print(f"  Age: {student_info['age']}")
            print(f"  Subject: {student_info['subject']}")
            print(f"  Grade: {student_info['grade']:.2f}")
            print(f"  Status: {status}")
    else:
        print("No students in the directory.")
