from tkinter import Tk, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)

        self.converter = Converter()
        km = 100
        miles = self.converter.get_miles_from_km (km)
        self.label = Label(self, text='km' + '' + str(km)).grid(row=2)
        self.label = Label(self, text='miles' + format(miles, '.2f')).grid(row=3)

        self.mainloop()

    
