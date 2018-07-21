from tkinter import *

import app

# Note to self: Currently trying to make buttons on toplevels

class Application:
    
    '''
    This is the home venue of the application
    '''
    
    def __init__(self, master):
        
        self.email1 = StringVar()

        self.master = master       
        self.master.title('Garment')

        mainmenu = Menu(self.master)
        self.master.config(menu = mainmenu)


        file = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'New', command = self.create_user)
        file.add_separator()
        file.add_command(label = 'Exit', command = root.quit)

        background = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'Settings', menu = background)
        background.add_command(label = 'Color', command = self.txtcolor)
        
        frame1 = Frame(self.master)
        frame1.pack(padx = 10, pady = 5)

        label = Label(frame1, text = 'Email')
        entry = Entry(frame1, textvariable = self.email1)
        label.pack()
        entry.pack()

        frame2 = Frame(self.master)
        frame2.pack()

        view_button = Button(frame2, text = 'VIEW', fg = 'blue', command = self.submit_view_user)
        delete_button = Button(frame2, text = 'delete', fg = 'red', command = self.delete_user)
        view_button.pack()
        delete_button.pack()



        self.text = Text(self.master)
        self.text.pack()
        self.text.insert(END, "")

    def txtcolor(self):
        pass



    def submit_view_user(self):
        self.text.insert(END, f'{app.view_customer(self.email1.get())}')

    def create_user(self):
        top = Toplevel(self.master)
        data = Create(top)

    def delete_user(self):
        top = Toplevel(self.master)
        data = Delete(top)


class Create:
        
    def __init__(self, master):
        
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email_ = StringVar()
        self.phone = IntVar()
            

        self.master = master
        self.master.title('Create User')
        # self.master.geometry('300 X 300')

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

        self.button1 = Button(self.master, text = 'submit', command = submit_new_user)
        self.button1.pack()


        def submit_new_user():
            name = self.firstname.get() + ' ' + self.lastname.get()
            app.add_customer(name, self.email_.get(), self.phone.get())


class Delete:
    
    def __init__(self, master):
        self.email_ = StringVar()
    
        self.master = master
        self.master.title('Delete User')

        self.email = Label(self.master, text ="Email")
        self.entry2 = Entry(self.master, textvariable = self.email_)
        self.email.pack()
        self.entry2.pack()

        self.submit = Button(self.master, text = 'submit', command = self.submit_delete_user)
        self.submit.pack()

    def submit_delete_user(self):
        confirm_delete = Toplevel()
        confirm_delete.title("Confirm Delete user")

        label = Label(confirm_delete, text = 'Are you sure you want to delete user?')
        delete_button = Button(confirm_delete, text = 'Delete', fg = 'red', command = conf_delete)
        cancel_button = Button(confirm_delete, text = 'cancel', command = confirm_delete.destroy)
        label.pack()
        delete_button.pack()
        cancel_button.pack()

        def conf_delete():
            app.delete_customer(self.email_.get())
    



root = Tk()
appl = Application(root)
root.mainloop()
