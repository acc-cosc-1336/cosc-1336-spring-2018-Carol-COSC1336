def recursive_decimal_binary(num, bits):
    '''
    Given a whole number from the decimal system, converts the number to 8-bit binary
    Given 86 returns 01010110
    :param num:
    :return:
    '''
    #bits are 0,1,2,3,4,5,6,7
    power_value = 2**bits  # power values 128,64,32,6,8,4,2,1
    if num == 0 and bits < 0:
        return ''
    elif num >= power_value:
        return '1' + recursive_decimal_binary(num-power_value, bits-1)
        
    else:
        return '0' + recursive_decimal_binary(num, bits-1)
