'''
Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the
proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings),
 we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that
your answer is allowed an absolute error of 0.001.

Sample Dataset
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Sample Output
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000

'''
def get_p_distance_matrix(dna_list):

    p_distance = [[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]
    #print(p_distance)
    #print(dna_list)
    r=0
    for sub_list in dna_list:
        r=r+1
        c=0
        p_sum = 0
        print(r,c)
    for r in range(r):
        while c < len(sub_list):
            if dna_list[r][c] != dna_list[r+1][c]:
                print(dna_list[r][c], dna_list[r+1][c])
                p_sum += 1
                c+=1
                print(p_sum)
    return p_sum

        
    #c=len(sub_list)

    #for r in range(r):
        #for c in range(c):
            #print(dna_list[r][c]) 


    #return p_distance
