from tkinter import *
import app

class Front:
    def __init__(self):
        window = Tk()
        window.title('Garment')
        frame1 = Frame(window)
        frame1.pack()

        label1 = Label(frame1, text = 'Email: ')
        self.email = StringVar()
        enter_email = Entry(frame1, textvariable = self.email)
        label1.grid(row = 1, column = 1)
        enter_email.grid(row = 1, column = 2)

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

        frame3 = Frame(window)
        frame3.pack()

        view_button = Button(frame3, text = 'View', command = self.display_customer_data)
        view_button.grid(row = 1, column = 1)

        self.text = Text(window)
        self.text.pack()
        self.text.insert(END, '')



        window.mainloop()

    def add_customer(self):
        customer_email = self.email.get()
        return customer_email

    def plus(self):
        pass

    def display_customer_data(self):
        self.text.insert(END, f'{app.view_customer(self.add_customer())}')
            
Front()
