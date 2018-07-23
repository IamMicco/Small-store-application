from tkinter import *

import app


class Application:
    
    '''
    This is the home venue of the application
    '''
    
    def __init__(self, master):
        
        self.email = StringVar()

        self.master = master       
        self.master.title('Garment')

        mainmenu = Menu(self.master)
        self.master.config(menu = mainmenu)


        file = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'New', command = self.create_user)
        file.add_command(label = 'Current', command = self.update_current_user)
        file.add_separator()
        file.add_command(label = 'Delete', command = self.delete_user)
        file.add_command(label = 'Exit', command = self.master.quit)

        background = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'Settings', menu = background)
        background.add_command(label = 'Color', command = self.txtcolor)
        
        frame1 = Frame(self.master)
        frame1.pack(padx = 10, pady = 5)

        label = Label(frame1, text = 'Email')
        entry = Entry(frame1, textvariable = self.email)
        label.pack()
        entry.pack()

        frame2 = Frame(self.master)
        frame2.pack()

        view_button = Button(frame2, text = 'VIEW', fg = 'blue', command = self.submit_view_user)
        view_button.pack()

        frame3 = Frame(self.master)
        frame3.pack()

        self.label2 = Label(frame3, text = None)
        self.label2.pack()


        self.text = Text(self.master)
        self.text.pack()
        self.text.insert(END, "")

    def txtcolor(self):
        pass



    def submit_view_user(self):
        self.text.delete(1.0,END)
        for item in app.view_customer(self.email.get()):
            self.text.insert(END, item)


    def create_user(self):
        top = Toplevel(self.master)
        data = Create(top)

    def update_current_user(self):
        top = Toplevel(self.master)
        data = Update(top)

    def delete_user(self):
        top = Toplevel(self.master)
        data = Delete_data(top)


class Create:
    
    '''
    Creates a new customer profile and adds it to the database
    '''
        
    def __init__(self, master):
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email_ = StringVar()
        self.phone = IntVar()
            

        self.master = master
        self.master.title('Create User')

        self.first_name = Label(self.master, text ="Firstname")
        self.entry1 = Entry(self.master, textvariable = self.firstname)
        self.first_name.pack()
        self.entry1.pack()

        self.last_name = Label(self.master, text ="Lastname")
        self.entry2 = Entry(self.master, textvariable = self.lastname)
        self.last_name.pack()
        self.entry2.pack()

        self.email = Label(self.master, text ="Email")
        self.entry3 = Entry(self.master, textvariable = self.email_)
        self.email.pack()
        self.entry3.pack()

        self.phone_number = Label(self.master, text = 'Phone number')
        self.entry4 = Entry(self.master, textvariable = self.phone)
        self.phone_number.pack()
        self.entry4.pack()

        self.button1 = Button(self.master, text = 'submit', command = self.submit_new_user)
        self.button1.pack()


    def submit_new_user(self):
        name = self.firstname.get() + ' ' + self.lastname.get()
        app.add_customer(name, self.email_.get(), self.phone.get())
        top = Toplevel(self.master)
        data = Create_user_items(top, self.email_.get())
        root.quit()

class Create_user_items:
    
    '''
    Adds the items bought to the created customer profile
    '''
    
    def __init__(self, master, email):
        self.master = master
        self.master.title('Add Items')

        self.email = email
        self.customer = app.find_customer(self.email)

        self.color1 = 'Red'
        self.color2 = 'Green'
        self.color3 = 'Black'
        self.color4 = 'Brown'
        self.color5 = 'Yellow'
        self.color6 = 'White'

        self.item_button1 = Button(self.master, text = 'Item1', command = self.add_color1)
        self.item_button2 = Button(self.master, text = 'Item2', command = self.add_color2)
        self.item_button3 = Button(self.master, text = 'Item3', command = self.add_color3)
        self.item_button4 = Button(self.master, text = 'Item4', command = self.add_color4)
        self.item_button5 = Button(self.master, text = 'Item5', command = self.add_color5)
        self.item_button6 = Button(self.master, text = 'Item6', command = self.add_color6)
        self.item_button1.pack()
        self.item_button2.pack()
        self.item_button3.pack()
        self.item_button4.pack()
        self.item_button5.pack()
        self.item_button6.pack()

    def add_color1(self):
        app.add_customer_items(self.customer, self.color1)

    def add_color2(self):
        app.add_customer_items(self.customer, self.color2)

    def add_color3(self):
        app.add_customer_items(self.customer, self.color3)

    def add_color4(self):
        app.add_customer_items(self.customer, self.color4)

    def add_color5(self):
        app.add_customer_items(self.customer, self.color5)

    def add_color6(self):
        app.add_customer_items(self.customer, self.color6)



class Update:
    
    '''
    Finds specified Customerand returns the object from the database
    '''
    
    def __init__(self, master):
        self.email_ = StringVar()

        self.master = master
        self.master.title('Find Customer')

        self.email = Label(self.master, text ="Email")
        self.entry = Entry(self.master, textvariable = self.email_)
        self.button = Button(self.master, text = 'Find User', command = self.update_information)
        self.email.pack()
        self.entry.pack()
        self.button.pack()

    def find_user(self):
        return app.find_customer(self.email_.get())

    def update_information(self):
        top = Toplevel(self.master)
        user = self.find_user()
        data = Update_info(top, user, self.email_)

class Update_info:
    
    '''
    With selected Customer objects, this class adds the new item to the selected customer profile
    '''
    
    def __init__(self, master, customer, email):
        self.customer = customer

        self.master = master
        self.master.title('Update Customer Items')

        self.email = email

        self.color1 = 'Red'
        self.color2 = 'Green'
        self.color3 = 'Black'
        self.color4 = 'Brown'
        self.color5 = 'Yellow'
        self.color6 = 'White'


        self.item_button1 = Button(self.master, text = 'Item1', command = self.add_color1)
        self.item_button2 = Button(self.master, text = 'Item2', command = self.add_color2)
        self.item_button3 = Button(self.master, text = 'Item3', command = self.add_color3)
        self.item_button4 = Button(self.master, text = 'Item4', command = self.add_color4)
        self.item_button5 = Button(self.master, text = 'Item5', command = self.add_color5)
        self.item_button6 = Button(self.master, text = 'Item6', command = self.add_color6)
        self.item_button1.pack()
        self.item_button2.pack()
        self.item_button3.pack()
        self.item_button4.pack()
        self.item_button5.pack()
        self.item_button6.pack()

    def add_color1(self):
        app.add_customer_items(self.customer, self.color1)

    def add_color2(self):
        app.add_customer_items(self.customer, self.color2)

    def add_color3(self):
        app.add_customer_items(self.customer, self.color3)

    def add_color4(self):
        app.add_customer_items(self.customer, self.color4)

    def add_color5(self):
        app.add_customer_items(self.customer, self.color5)

    def add_color6(self):
        app.add_customer_items(self.customer, self.color6)

        


class Delete_data:
    
    '''
    This finds specific customer and deletes his/her profile
    '''
    
    def __init__(self, master):
        self.email = StringVar()
    
        self.master = master
        self.master.title('Delete User')

        self.label = Label(self.master, text ="Email")
        self.entry = Entry(self.master, textvariable = self.email)
        self.label.pack()
        self.entry.pack()

        self.delete = Button(self.master, text = 'Delete', command = self.confirm_delete_user)
        self.exit = Button(self.master, text = 'Exit', command = root.quit)
        self.delete.pack()

    def confirm_delete_user(self):
        top = Toplevel(self.master)
        data = Confirm(top, self.email)


class Confirm:
    
    '''
    This asks the Customer if he/she is sure of the profile deletion
    '''
    
    def __init__(self, master, email):
        self.email = email
        
        self.master = master
        self.master.title('Confirm Deletion')

        self.label = Label(self.master, text = 'Are you sure you want to delete customer?')
        self.delete_button = Button(self.master, text = 'Delete', fg = 'red', command = self.conf_delete)
        self.cancel_button = Button(self.master, text = 'Cancel', fg = 'grey', command = self.master.quit)
        self.label.pack()
        self.delete_button.pack()
        self.cancel_button.pack()
        

    def conf_delete(self):
        app.delete_customer(self.email.get())
    



root = Tk()
appl = Application(root)
root.mainloop()
