from tkinter import *

import app


class App:
    def __init__(self):
        window = Tk()
        window.title('Garment')

        mainmenu = Menu(window)
        window.config(menu = mainmenu)


        file = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'New', command = create_user)
        
        frame1 = Frame(window)
        frame1.pack(padx = 10, pady = 5)

        label = Label(frame1, text = 'Email').grid(row = 1, column = 1)
        self.email1 = StringVar()
        entry = Entry(frame1, textvariable = self.email1).grid(row = 1, column = 2)

        frame2 = Frame(window)
        frame2.pack()

        view_button = Button(frame2, text = 'VIEW', fg = 'blue', command = self.submit_view_user).grid(row = 1, column = 1, sticky = W)
        delete_button = Button(frame2, text = 'delete', fg = 'red', command = delete_customer).grid(row = 1, column = 2, sticky = E)



        self.text = Text(window)
        self.text.pack()
        self.text.insert(END, "")

        window.mainloop()

    def submit_view_user(self):
        self.text.insert(END, f'{app.view_customer(self.email1.get())}')

    # def submit_delete_user(self):
    #     app.delete_customer(self.email1.get())




def create_user():
    top=Toplevel()
    top.title("Create user")

    first_name = Label(top, text ="Firstname", font=('Times', 15)).grid(row=0,column=0, sticky=W)
    firstname = StringVar()
    entry1 = Entry(top, textvariable = firstname).grid(row = 0, column = 1)

    last_name = Label(top, text ="Lastname", font=('Times', 15)).grid(row=1,column=0, sticky=W)
    lastname = StringVar()
    entry2 = Entry(top, textvariable = lastname).grid(row = 1, column = 1)

    email = Label(top, text ="Email", font=('Times', 15)).grid(row=2,column=0, sticky=W)
    email_ = StringVar()
    entry3 = Entry(top, textvariable = email_).grid(row = 2, column = 1)

    phone_number = Label(top, text = 'Phone number', font = ('Times', 15)).grid(row = 3, column = 0, sticky = W)
    phone = IntVar()
    entry4 = Entry(top, textvariable = phone).grid(row = 3, column = 1, sticky = W)

    button1 = Button(top, text = 'submit', command = submit_new_user).grid(row = 4, column = 1, columnspan = 2, sticky = W)
    button1.pack()



    def submit_new_user():
        name = firstname.get() + ' ' + lastname.get()
        app.add_customer(name, email_.get(), phone.get())

def view_customer():
    view = Toplevel()
    view.title("View user")

    email = Label(view, text ="Email", font=('Times', 15))
    email.grid(row=2,column=0, sticky=W)
    email_ = StringVar()
    entry2 = Entry(view, textvariable = email_).grid(row = 2, column = 1)

    submit = Button(view, text = 'submit', command = submit_view_user)

    def submit_view_user():
        App().text.insert(END, f'{app.view_customer(email_.get())}')


def delete_customer():
    view = Toplevel()
    view.title("Delete user")

    email = Label(view, text ="Email", font=('Times', 15))
    email.grid(row=2,column=0, sticky=W)
    email_ = StringVar()
    entry2 = Entry(view, textvariable = email_).grid(row = 2, column = 1)

    submit = Button(view, text = 'submit', command = submit_delete_user)

    def submit_delete_user():
        confirm_delete = Toplevel()
        confirm_delete.title("Confirm Delete user")

        label = Label(confirm_delete, text = 'Are you sure you want to delete user?').grid(row = 1, colummn = 1, sticky = W)
        delete_button = Button(confirm_delete, text = 'Delete', fg = 'red', command = conf_delete).grid(row = 1, colummn = 1, sticky = W)
        cancel_button = Button(confirm_delete, text = 'cancel', command = confirm_delete.destroy).grid(row = 1, column = 2, sticky = W)

        def conf_delete():
            app.delete_customer(email_.get())

    




App()
