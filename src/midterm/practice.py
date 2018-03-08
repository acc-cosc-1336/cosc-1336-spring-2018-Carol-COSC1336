def get_km_per_hour(miles, total_minutes):
    '''
    Write a program that asks user for miles ridden on a bike and the total time ridden. Display average
    speed per hour in kilometers
    CREATE A TEST CASE FOR THIS FUNCTION
    :param miles:  Miles ridden on a bike
    :param total_minutes: Total minutes elapsed
    :return: Average speed per hour to hundredths place
    '''
    #following lines commented out in order to get test to run
    #miles = float(input('Enter number of miles ridden: '))
    #total_minutes = int(input('Enter total minutes elapsed: '))

    hours = total_minutes / 60
    
    return round(miles / hours * 1.6, 2)


'''
Create a function get_shipping_charge with one parameter named weight 
that returns rate per pound according to this table.
CREATE A TEST CASE FOR THIS FUNCTION

Weight                      Rate per Pound
0 to 2                      1.25
Over 2 but less than eq 6      2.75
Over 6 but less than eq 10     3.75
Over 10                     4.50

'''
def get_shipping_charge(weight):

    if weight >= 0 and weight <=2:
        return 1.25
    elif weight > 2 and weight <= 6:
        return 2.75
    elif weight > 6 and weight <= 10:
        return 3.75
    elif weight > 10:
        return 4.5
    else:
        return 'Invalid weight range'

'''
Create a function get_total_of_numbers_squared with a parameter named num
tha returns the total sum of the numbers squared.
CREATE A TEST CASE FOR THIS FUNCTION 

Sample Data
param num value 5
0
1
4
9
16

Returns 30
'''
def get_total_of_numbers_squared(num):
    i = 0
    total = 0
    while i < num:
        total += i ** 2
        i += 1

    return total


'''
Create a function get_quiz_list that returns a list of students
that have more than six quiz scores.
CREATE A TEST CASE FOR THIS FUNCTION.
Sample Data:
[
['joe', 10, 15, 20, 30, 40],
['bill', 23, 16, 19, 22],
['sue', 8 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17],
['grace', 12, 28, 21, 45, 26, 10, 11],
['john', 14, 32, 25, 16, 89]
]

Return Value:
['Sue','grace']

'''
def get_quiz_list(list1):

    return_list = []

    for sub_list in list1:
        if len(sub_list) > 7:
            return_list.append(sub_list[0])

    return return_list

def get_quiz_list_file():
    file = open('/home/travis/build/acc-cosc-1336/cosc-1336-spring-2018-Carol-COSC1336/src/midterm/quiz.dat', 'r')
    return_list = []

    for line in file:
        list1 = line.split()
        #print(list1)
        if len(list1) > 7:
            return_list.append(list1[0])

    file.close()

    return  return_list

    
    
    
