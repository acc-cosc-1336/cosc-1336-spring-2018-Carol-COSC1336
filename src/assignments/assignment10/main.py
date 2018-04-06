#Write import statements for classes invoice and invoice_item and PRODUCT
#from src.assignments.assignment10.invoice import  Invoice
#from src.assignments.assignment10.invoice_item import  InvoiceItem
#from src.assignments.assignment10.product import  Product
#from src.assignments.assignment10.customer import  Customer

from invoice import  Invoice
from invoice_item import  InvoiceItem
from product import  Product
from customer import  Customer

#ASSIGNMENT10 Write import statements for classes product and customer


'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
#ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class 
customer = Customer('John', 'Doe', '555-5555')
invoice = Invoice(customer, 'April 5')

keep_going = 'y'

while keep_going == 'y':

    product_id = input('Enter Product ID: ')
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))

    #ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.
    #Quantity parameter remains same.
    product = Product(product_id, cost, product_name)
    invoice.add_invoice_item(InvoiceItem(product, quantity))

    keep_going = input("Enter another type y: ")


invoice.print_invoice()




