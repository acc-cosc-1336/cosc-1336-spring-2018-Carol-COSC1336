#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average

from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average

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
    index = int(input('Enter the number of students for grade input: '))
    for index in range (index):
        grades_per_student = int(input('Enter the number of classes taken by student: '))
        total_grade_points = 0
        total_credit_hours = 0
        for grades_per_student in range (grades_per_student):
            letter_grade = input('Enter your letter grade for each class completed: ')
            result1 = valid_letter_grade(letter_grade)
            credit_points = get_credit_points(result1)

            credit_hours = int(input('Enter the number of credit hours for the above class: '))
            result3 = get_grade_points(credit_hours, credit_points) #only one class, need to accumulate
            total_grade_points = total_grade_points + result3
            print ('Student Total Grade Points are: ', total_grade_points)
            total_credit_hours = total_credit_hours + credit_hours
            print ('Student Total Credit Hours are: ', total_credit_hours)
            result4 = get_grade_point_average(total_credit_hours,total_grade_points)
            print('Student GPA is: ', result4)
    
               

#CALL THE MAIN FUNCTION
main()

