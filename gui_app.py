from tkinter import *
from app import Customer, Garment, initialize, menu_loop, add_customer

class Front:
    def __init__(self):
        window = Tk()
        window.title('Garment')
        frame1 = Frame(window)
        frame1.pack()

        label1 = Label(frame1, text = 'Email: ')
        self.email = StringVar()
        enteremail = Entry(frame1, textvariable = self.email)
        label1.grid(row = 1, column = 1)
        enteremail.grid(row = 1, column = 2)

        frame2 = Frame(window)
        frame2.pack()

        label2 = Label(frame2, text='Color: ')
        self.color = StringVar()
        self.b1 = IntVar()
        enter_color = Entry(frame2, textvariable = self.color)
        add_btn = Button(frame2, text='Add', command=self.plus)
        label2.grid(row = 1, column = 1)
        enter_color.grid(row = 1, column = 2)
        add_btn.grid(row = 1, column = 3)



        window.mainloop()

    def add_customer(self):
        customer_email = self.email.get()
        return customer_email

    def plus(self):
        
        pass
            
Front()