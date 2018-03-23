#write import statement for homework 7 file
from src.homework.homework7 import get_p_distance_matrix
'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''

def main():

    file = open('p_distance.dat', 'r')
    return_list = []
    for line in file:
        list1 = line.split()
        return_list.append(list1)
    
    p_distance = get_p_distance_matrix(return_list)

    file.close()
    print(p_distance)

main()

    

            
        
