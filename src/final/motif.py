
def non_contiguous_motif(str1, dna_list):
    dna_list = "".join(str(x) for x in dna_list)
    index=0
    position = 0
    position_list = []
    for index in range (0, len(str1)):
        position = dna_list.find(str1[index])
        position_list.append(position+1)
        index +=1
    return tuple(position_list)
