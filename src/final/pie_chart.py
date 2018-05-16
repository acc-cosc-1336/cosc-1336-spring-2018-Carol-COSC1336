from pie_arc import PieArc

class PieChart(PieArc):

    def __init__(self, text):

        PieArc.__init__(self,text)

    def draw(self):

        print(self.text)        

                    
