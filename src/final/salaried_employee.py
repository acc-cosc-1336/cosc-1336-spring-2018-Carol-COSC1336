from employee import Employee

class SalariedEmployee (Employee):

    def __init__(self, employee_id, name, yearly_rate):

        Employee.__init__(self, employee_id, name)

        self.yearly_rate = yearly_rate
            
    def calculate(self):
        return self.yearly_rate/26
