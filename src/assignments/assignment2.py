def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    '''
    Write code to calculate faculty evaluation rating according to asssignment instructions
    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''
    #find total first, then find ratios
    total = nev + rar + som + + oft + voft + alw
    alw_ratio = alw/total
    voft_ratio = voft/total
    oft_ratio = oft/total
    som_ratio = som/total
    rar_ratio = rar/total
    nev_ratio = nev/total
    
    if voft_ratio + alw_ratio >= .90:
            return 'Excellent'
    elif oft_ratio + voft_ratio + alw_ratio >= .80:
            return 'Very Good'
    elif som_ratio + oft_ratio + voft_ratio + alw_ratio >= .70:
            return 'Good'
    elif rar_ratio + som_ratio + oft_ratio + voft_ratio + alw_ratio >= .60:
            return 'Needs Improvement'
    else:
            return 'Unacceptable'
            
		
		
def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
