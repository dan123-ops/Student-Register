
temp_file = open("reg_form.txt", "a")

exam_register = " "

student_register_no = int(input("Please enter the amount of students registering for this examination!: "))

# This for loop will store information into 'exam_register'
# The loop runs for as many times as the number entered for 'student_register_no'
# Each time the next student is asked to enter their id number
# The id number is stored on a new line which is proceeded by a dotted line for the student to sign
# I have printed the result onto the console so, as to compare with what is written into the file
for idx in range(student_register_no):
    student_id = str(input("Please can the next student enter their ID number!: "))
    exam_register = exam_register + "Student ID: " + student_id + "\n" + "Sign here: ______________" + "\n" + "\n"
print(exam_register)

temp_file.close()

# This will open and write the stored information in exam_register to '?' (?, " ")
# The write function is based on the letter at '?' (" ", ?)
with open("reg_form.txt", "w") as f:
    f.write(exam_register)
