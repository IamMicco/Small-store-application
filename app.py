from peewee import *
from collections import OrderedDict
from datetime import datetime

import gui_app

db = SqliteDatabase('garment.db')

class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    id = PrimaryKeyField(null=False)
    email = CharField(unique=True)


class Garment(BaseModel):
    id = PrimaryKeyField(null=False)
    color = CharField(max_length=20)
    time_stamp = DateTimeField(default=datetime.now)
    customer = ForeignKeyField(Customer, related_name='customer_details')


def initialize():
    db.connect()
    db.create_tables([Customer], safe=True)
    db.create_tables([Garment], safe=True)

def menu_loop():
    choice = None
    while choice != 'q':
        print ('Make a choice')
        for key, value in menu.items():
            print (f'{key}), {value.__doc__}')

        choice = input('Action: ').lower().strip()
        if choice in menu:
            if menu[choice] == view_customer or menu[choice] == delete_customer:
                email = input('Enter email: ')
                menu[choice](email)
            else:
                menu[choice]()


def add_customer():
    '''Add Customer'''
    # customer_email = input('Enter customer email: ')
    customer = Customer.create(email=gui_app.Front().add_customer())
    action = None
    while action != 'yes':
        customer_purchase = input('Enter products color: ').strip()
        Garment.create(customer=customer, color=customer_purchase)
        action = input('Are you done? yes/no').lower().strip()



def view_customer(email=None):
    '''View customers'''
    if email:
        customer = Customer.get(email==email)
        count = 1
        for garment in customer.customer_details:
            time_stamp = garment.time_stamp.strftime('%A %B %d, %Y %I:%M%p')
            count += 1
            return (('='*len(time_stamp)) + '\n' + (time_stamp) + 'n' + ('='*len(time_stamp)) + '\n' + (f'{count}: {garment.color}') + '\n' + ('='*len(time_stamp)) + '\n')


def delete_customer(email=None):
    '''Delete customer'''
    customer = Customer.get(Customer.email==email)
    if customer:
        if input('Are you sure that you want to delete the given customer? Y/N').lower().strip() == 'y':
            customer.delete_instance()
        
        

menu = OrderedDict([
    ('a', add_customer),
    ('v', view_customer),
    ('d', delete_customer),
])

if __name__ == '__main__':
    initialize()
    menu_loop()


