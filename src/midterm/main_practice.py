#write import statement for get_total_of_numbers_squared
#from practice import get_total_of_numbers_squared
from src.midterm.practice import get_total_of_numbers_squared

'''
Write a main function to ...
Loop until user opts not to.
Prompt user for a number.
Call the get_total_of_numbers_squared function with prompted number as argument.
Display the return value of get_total_of_numbers_squared function.
'''

#Call the main function

def main():

    again = 'Y'
    while again == 'y' or again == 'Y':
        num = int(input('Enter a number: '))
        total = get_total_of_numbers_squared(num)
        
        print('The total of your numbers squared = ', total)
        print('Do you want to enter another number?')
        again = input('y = yes, anything else = no: ')

main()
