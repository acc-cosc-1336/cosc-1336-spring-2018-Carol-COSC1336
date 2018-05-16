from salaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee

employees = {1:HourlyEmployee(1,'joe',10,80),2:SalariedEmployee(2, 'Mike', 80000)} 

for value in employees.values():
    value.calculate()
    print (format(value.calculate(), '.2f'))
    
