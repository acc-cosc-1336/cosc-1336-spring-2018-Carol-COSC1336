#write import statement for reverse string function
from src.midterm.exam import reverse_string
#from exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():

    again = 'Y'
    while again == 'y' or again == 'Y':
        string1 = input('Enter a string: ')
        string1_rev = reverse_string(string1)
        print('Your string reversed: ',string1_rev )
        again = input('y = yes, anything else = no: ')

main()
