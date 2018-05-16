class Player:

    def __init__(self,true_false,d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.true_false = true_false

    def check_come_out_roll(self):
        while self.true_false == True or self.true_false == False:
            if self.d1+self.d2 > 12:
                print('Invalid range')
                return 'Invalid range'
            while self.true_false == True:
                if self.d1+self.d2 == 7 or self.d1+self.d2 == 11:
                    print ('Winner')
                    return 'Winner'
                elif self.d1+self.d2 == 2 or self.d1+self.d2 == 3 or self.d1+self.d2 == 12:
                    print('Loser')
                    return 'Loser'
                else:
                    print (self.d1+self.d2)
                    return (self.d1+self.d2)
            while self.true_false == False:
                if self.d1+self.d2 == 7 or self.d1+self.d2 == 11:
                    print('Loser')
                    return 'Loser'
                elif self.d1+self.d2 == 2 or self.d1+self.d2 == 3 or self.d1+self.d2 == 12:              
                    print ('Winner')
                    return 'Winner'
                else:
                    print (self.d1+self.d2)
                    return self.d1+self.d2
        
            

            
            
        
        
