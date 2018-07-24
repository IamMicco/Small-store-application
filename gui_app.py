from tkinter import *

import app


class Application:
    
    '''
    This is the home venue for the application
    '''
    
    def __init__(self, master):
        
        self.email = StringVar()

        self.master = master       
        self.master.title('Retail App')

        icon = PhotoImage(file = 'icons.png')
        self.master.call('wm', 'iconphoto', self.master._w, icon)

        mainmenu = Menu(self.master)
        self.master.config(menu = mainmenu)


        file = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'New', command = self.create_user)
        file.add_command(label = 'Current', command = self.update_current_user)
        file.add_separator()
        file.add_command(label = 'Delete', command = self.delete_user)
        file.add_command(label = 'Exit', command = self.master.destroy)

        background = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'Settings', menu = background)
        background.add_command(label = 'Color', command = self.txtcolor)
        
        frame1 = Frame(self.master)
        frame1.pack(padx = 10, pady = 5)

        label = Label(frame1, text = 'Email').grid(row = 1, column = 1)
        entry = Entry(frame1, textvariable = self.email).grid(row = 1, column = 2)

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
        try:
            for item in app.view_customer(self.email.get()):
                self.text.insert(END, item)
        except ValueError:
            top = Toplevel(self.master)
            data = Popup_message(top)
        except TypeError:
            top = Toplevel(self.master)
            data = Popup_Empty(top)


    def create_user(self):
        top = Toplevel(self.master)
        data = Create(top)

    def update_current_user(self):
        top = Toplevel(self.master)
        data = Update(top)

    def delete_user(self):
        top = Toplevel(self.master)
        data = Delete_data(top)

class Popup_message:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Popup message!')

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.label = Label(self.master, text = 'Data not in database, please check spelling')
        self.button = Button(self.master, text = 'Ok',command =self.master.destroy)
        self.label.pack()
        self.button.pack()


class Popup_Empty:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Popup message!')

        icon = PhotoImage(file = 'icons.png')
        self.master.call('wm', 'iconphoto', self.master._w, icon)

        self.label = Label(self.master, text = 'Entry box cannot be left empty')
        self.button = Button(self.master, text = 'Ok',command =self.master.destroy)
        self.label.pack()
        self.button.pack()


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

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.first_name = Label(self.master, text ="Firstname").grid(row = 1, column = 1, sticky = W)
        self.entry1 = Entry(self.master, textvariable = self.firstname).grid(row = 1, column = 2, sticky = W)

        self.last_name = Label(self.master, text ="Lastname").grid(row = 2, column = 1, sticky = W)
        self.entry2 = Entry(self.master, textvariable = self.lastname).grid(row = 2, column = 2, sticky = W)

        self.email = Label(self.master, text ="Email").grid(row = 3, column = 1, sticky = W)
        self.entry3 = Entry(self.master, textvariable = self.email_).grid(row = 3, column = 2, sticky = W)

        self.phone_number = Label(self.master, text = 'Phone number').grid(row = 4, column = 1, sticky = W)
        self.entry4 = Entry(self.master, textvariable = self.phone).grid(row = 4, column = 2, sticky = W)

        self.button1 = Button(self.master, text = 'submit', command = self.submit_new_user).grid(row = 5)


    def submit_new_user(self):
        name = self.firstname.get() + ' ' + self.lastname.get()
        app.add_customer(name, self.email_.get(), self.phone.get())
        top = Toplevel(self.master)
        data = Create_user_items(top, self.email_.get())

class Create_user_items:
    
    '''
    Adds the items bought to the created customer profile
    '''
    
    def __init__(self, master, email):
        self.master = master
        self.master.title('Add Items')

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.email = email
        self.customer = app.find_customer(self.email)

        self.color1 = 'Red'
        self.color2 = 'Green'
        self.color3 = 'Black'
        self.color4 = 'Brown'
        self.color5 = 'Yellow'
        self.color6 = 'White'

        self.item_button1 = Button(self.master, text = 'Item1', command = self.add_color1).grid(row = 1, column = 1, sticky = W)
        self.item_button2 = Button(self.master, text = 'Item2', command = self.add_color2).grid(row = 1, column = 3, sticky = W)
        self.item_button3 = Button(self.master, text = 'Item3', command = self.add_color3).grid(row = 1, column = 5, sticky = W)
        self.item_button4 = Button(self.master, text = 'Item4', command = self.add_color4).grid(row = 2, column = 1, sticky = W)
        self.item_button5 = Button(self.master, text = 'Item5', command = self.add_color5).grid(row = 2, column = 3, sticky = W)
        self.item_button6 = Button(self.master, text = 'Item6', command = self.add_color6).grid(row = 2, column = 5, sticky = W)
        self.item_button7 = Button(self.master, text = 'Ok', command = self.master.destroy).grid(row = 3, column = 3)

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

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.email = Label(self.master, text ="Email").grid(row = 1, column = 1, sticky = W)
        self.entry = Entry(self.master, textvariable = self.email_).grid(row = 1, column = 2, sticky = W)
        self.button = Button(self.master, text = 'Find User', command = self.update_information).grid(row = 2, column = 2)

    def find_user(self):
        return app.find_customer(self.email_.get())

    def update_information(self):
        try:
            user = self.find_user()
        except ValueError:
            notice = Toplevel(self.master)
            stop = Pop_up(notice)
        else:
            top = Toplevel(self.master)
            data = Update_info(top, user, self.email_)


class Update_info:
    
    '''
    With selected Customer objects, this class adds the new item to the selected customer profile
    '''
    
    def __init__(self, master, customer, email):
        self.customer = customer

        self.master = master
        self.master.title('Update Customer Items')

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.email = email

        self.color1 = 'Red'
        self.color2 = 'Green'
        self.color3 = 'Black'
        self.color4 = 'Brown'
        self.color5 = 'Yellow'
        self.color6 = 'White'

        self.item_button1 = Button(self.master, text = 'Item1', command = self.add_color1).grid(row = 1, column =1, sticky = W)
        self.item_button2 = Button(self.master, text = 'Item2', command = self.add_color2).grid(row = 1, column =3, sticky = W)
        self.item_button3 = Button(self.master, text = 'Item3', command = self.add_color3).grid(row = 1, column =5, sticky = W)
        self.item_button4 = Button(self.master, text = 'Item4', command = self.add_color4).grid(row = 2, column =1, sticky = W)
        self.item_button5 = Button(self.master, text = 'Item5', command = self.add_color5).grid(row = 2, column =3, sticky = W)
        self.item_button6 = Button(self.master, text = 'Item6', command = self.add_color6).grid(row = 2, column =5, sticky = W)
        self.item_button7 = Button(self.master, text = 'Ok', command = self.master.destroy).grid(row = 3, column =3)

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



class Pop_up:
    
    def __init__(self, master):
        self.master = master
        self.master.title('Popup message!')

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.label = Label(self.master, text = 'Customer profile not in database, please check spelling')
        self.button = Button(self.master, text = 'Ok',command = self.master.destroy)
        self.label.pack()
        self.button.pack()


class Delete_data:
    
    '''
    This finds specific customer and deletes his/her profile
    '''
    
    def __init__(self, master):
        self.email = StringVar()
    
        self.master = master
        self.master.title('Delete User')

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.label = Label(self.master, text ="Email")
        self.entry = Entry(self.master, textvariable = self.email)
        self.label.pack()
        self.entry.pack()

        self.delete = Button(self.master, text = 'Delete', command = self.confirm_delete_user)
        self.exit = Button(self.master, text = 'Exit', command = self.master.destroy)
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

        icon = PhotoImage(file = 'icons.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, icon)

        self.label = Label(self.master, text = 'Are you sure you want to delete customer?').grid(row = 1)
        self.delete_button = Button(self.master, text = 'Delete', fg = 'red', command = self.conf_delete).grid(row = 2, column = 1)
        self.cancel_button = Button(self.master, text = 'Cancel', fg = 'grey', command = self.master.destroy).grid(row = 2, column = 2)
        

    def conf_delete(self):
        app.delete_customer(self.email.get())
        self.master.destroy()
    



root = Tk()
appl = Application(root)
root.mainloop()
