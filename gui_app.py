from tkinter import *
import app


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('Garment')
        self.geometry("300x300")
        
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        menubar = Menu(container)
        file = Menu(menubar, tearoff = 0)
        file.add_command(label = 'create user', command = lambda: popupmsg('Not supported yet'))
        menubar.add_cascade(label = "File", menu = file)
        file.add_command(label = "Add", command = lambda: Add)
        file.add_command(label = 'View', command = lambda: View)
        file.add_separator()
        file.add_command(label = 'Delete', command = lambda: Delete)

        

        Tk.config(self, menu=menubar)

        def popupmsg(message):
            pass

        self.frames = {}

        for F in (Add, View, Delete):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0)

        self.show_frame(Add)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

class Add(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = 'Add Page')
        label.pack(pady = 10, padx = 10)

        button1 = Button(self, text = 'View Page', command = lambda: controller.show_frame(View))
        button1.pack()

        button1 = Button(self, text = 'Delete Page', command = lambda: controller.show_frame(Delete))
        button1.pack()

class View(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = 'View Page')
        label.pack(pady = 10, padx = 10)

        button1 = Button(self, text = 'Back to Home', command = lambda: controller.show_frame(Add))
        button1.pack()


class Delete(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = 'Delete Page')
        label.pack(pady = 10, padx = 10)

        button1 = Button(self, text = 'Back to Home', command = lambda: controller.show_frame(Add))
        button1.pack()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
