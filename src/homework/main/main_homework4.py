#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
#KEEP FOR FINAL SUBMISSION from src.homework.homework4 import valid_letter_grade
from homework4 import valid_letter_grade
'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():
    index = int(input('Enter the number of students with grades: '))
    for index in range (1, index+1):
        letter_grade = input('Enter your letter grade for each class completed: ')
        result = valid_letter_grade(letter_grade)
        print(result)

    



#CALL THE MAIN FUNCTION
main()
