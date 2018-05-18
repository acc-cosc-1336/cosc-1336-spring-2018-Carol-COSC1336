from pie_arc import PieArc

class PieChart(PieArc):

    def __init__(self, list_pie_arcs):

        self.list_pie_arcs = list_pie_arcs

    def draw(self):

        for arc in self.list_pie_arcs:
            
            arc.draw()

                    
