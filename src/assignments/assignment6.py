def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''

    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for ch in dna_string:
        if ch == 'a' or ch == 'A':
            countA = countA + 1
        if ch == 'c' or ch == 'C':
            countC = countC + 1
        if ch == 'g' or ch == 'G':
            countG = countG + 1
        if ch == 't' or ch == 'T':
            countT = countT + 1

    return countA, countC, countG, countT


