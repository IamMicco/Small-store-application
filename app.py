from peewee import *
from datetime import datetime


db = SqliteDatabase('garment.db')

class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(null = False)
    email = CharField(unique=True)
    phone_number = IntegerField(null = False, unique = True)


class Garment(BaseModel):
    id = PrimaryKeyField(null=False)
    color = CharField(max_length=20)
    time_stamp = DateTimeField(default=datetime.now)
    customer = ForeignKeyField(Customer, related_name='customer_details')


def initialize():
    db.connect()
    db.create_tables([Customer, Garment], safe=True)


def add_customer(name = None, email = None, phone = None):
    '''Add Customer'''

    customer = Customer.create(name = name, email=email, phone_number = phone)
   

def add_customer_items(customer = None, color = None):
    if customer != None and color != None:
        Garment.create(customer = customer, color = color)

def current_customer(customer = None, color = None):
    '''Add to current Customer'''

    if customer != None and color != None:
        Garment.create(customer = customer, color = color)
  

def find_customer(email = None):
    try:

        customer = Customer.get(Customer.email==email)

    except Exception:
        return ValueError
    else:
        return customer


def view_customer(email=None):
    '''View customers'''
    if email:
        try:
            customer = Customer.get(Customer.email==email)
        except Exception:
            raise ValueError
        else:
            count = 0
            result = []
            for garment in customer.customer_details:
                time_stamp = garment.time_stamp.strftime('%A %B %d, %Y %I:%M%p')
                count += 1
                result.append(('='*len(time_stamp)) + '\n' + (time_stamp) + '\n' + ('='*len(time_stamp)) + '\n' + (f'{count}: {garment.color}') + '\n' + ('='*len(time_stamp)) + '\n')
            return result

    
def delete_customer(email=None):
    '''Delete customer'''
    customer = Customer.get(Customer.email==email)
    if customer:
        customer.delete_instance()
        


if __name__ == '__main__':
    initialize()
