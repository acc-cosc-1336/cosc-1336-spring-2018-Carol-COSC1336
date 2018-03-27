'''
Write a function named add_inventory with a widgets parameter of type dictionary, widget_name, and quantity

The function will add the widget to the dictionary if it doesn't exist.
If the widget exists it will update the quantity of the widgets.

    :param widgets:    a dictionary of widgets. Key is widget name, value is quantity
    :param widget_name: Widget name
    :param quantity:    Running count of inventory on hand
    :return:
'''
def add_inventory(widgets, widget_name, quantity):

    if widget_name not in widgets:
        widgets[widget_name] = quantity
        print('1st if - NOT IN', widgets)
    else:
        count = widgets[widget_name]
        quantity += count
        print('2nd if - IN', widgets)
  
    return quantity
            

'''
Write a function named remove_inventory_widget with a widget_name parameter.

The function will remove the widget_name if it exists and return 'Record deleted'
Otherwise it returns 'Item not found'

    :param widgets:
    :param widget_name:
    :return:
'''
def remove_inventory_widget(widget_name):

    widgets={}

    if widget_name in widgets:
        del widgets['widget_name']
        print('Record Deleted')
    else:
        if widget_name not in widgets:
            print('Item not found')
