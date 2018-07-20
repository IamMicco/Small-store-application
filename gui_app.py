from tkinter import *

import app


class Application:
    
    def __init__(self, master):
        self.email1 = StringVar()

        self.master = master       
        self.master.title('Garment')

        mainmenu = Menu(self.master)
        self.master.config(menu = mainmenu)


        file = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'New', command = self.create_user1)
        file.add_separator()
        file.add_command(label = 'Exit', command = root.quit)

        background = Menu(mainmenu, tearoff = 0)
        mainmenu.add_cascade(label = 'Background', menu = background)
        background.add_command(label = 'Color', command = self.bgcolor)
        
        frame1 = Frame(self.master)
        frame1.pack(padx = 10, pady = 5)

        label = Label(frame1, text = 'Email').grid(row = 1, column = 1)
        entry = Entry(frame1, textvariable = self.email1).grid(row = 1, column = 2)

        frame2 = Frame(self.master)
        frame2.pack()

        view_button = Button(frame2, text = 'VIEW', fg = 'blue', command = self.submit_view_user).grid(row = 1, column = 1, sticky = W)
        delete_button = Button(frame2, text = 'delete', fg = 'red', command = delete_customer).grid(row = 1, column = 2, sticky = E)



        self.text = Text(self.master)
        self.text.pack()
        self.text.insert(END, "")

    def bgcolor(self):
        pass



    def submit_view_user(self):
        self.text.insert(END, f'{app.view_customer(self.email1.get())}')

    def create_user1(self):
        top = Toplevel(self.master)
        data = Top(top)



class Top:
        
    def __init__(self, master):
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.email_ = StringVar()
        self.phone = IntVar()
            

        self.master = master
        # self.master.geometry('500X200')
        self.master.title('Create User')

        self.first_name = Label(self.master, text ="Firstname", font=('Times', 15)).grid(row=0,column=0, sticky=W)
        self.entry1 = Entry(self.master, textvariable = self.firstname).grid(row = 0, column = 1)

        self.last_name = Label(self.master, text ="Lastname", font=('Times', 15)).grid(row=1,column=0, sticky=W)
        self.entry2 = Entry(self.master, textvariable = self.lastname).grid(row = 1, column = 1)

        self.email = Label(self.master, text ="Email", font=('Times', 15)).grid(row=2,column=0, sticky=W)
        self.entry3 = Entry(self.master, textvariable = self.email_).grid(row = 2, column = 1)

        self.phone_number = Label(self.master, text = 'Phone number', font = ('Times', 15)).grid(row = 3, column = 0, sticky = W)
        self.entry4 = Entry(self.master, textvariable = self.phone).grid(row = 3, column = 1, sticky = W)

        self.button1 = Button(self.master, text = 'submit', command = submit_new_user).grid(row = 4, column = 1, columnspan = 2, sticky = W)
        self.button1.pack()


        def submit_new_user():
            name = self.firstname.get() + ' ' + self.lastname.get()
            app.add_customer(name, self.email_.get(), self.phone.get())




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

    



root = Tk()
appl = Application(root)
root.mainloop()
