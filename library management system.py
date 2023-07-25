import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class LibraryManagement(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("600x300")

        self.label1 = ttk.Label(self, text="Book ID")
        self.label2 = ttk.Label(self, text="Book Title")
        self.label3 = ttk.Label(self, text="Author")
        self.label4 = ttk.Label(self, text="Publisher")
        self.label5 = ttk.Label(self, text="Year of Publication")
        self.label6 = ttk.Label(self, text="ISBN")
        self.label7 = ttk.Label(self, text="Number of Copies")

        self.textField1 = ttk.Entry(self, width=10)
        self.textField2 = ttk.Entry(self, width=20)
        self.textField3 = ttk.Entry(self, width=20)
        self.textField4 = ttk.Entry(self, width=20)
        self.textField5 = ttk.Entry(self, width=10)
        self.textField6 = ttk.Entry(self, width=20)
        self.textField7 = ttk.Entry(self, width=10)

        self.addButton = ttk.Button(self, text="Add", command=self.add_book)
        self.viewButton = ttk.Button(self, text="View", command=self.view_books)
        self.editButton = ttk.Button(self, text="Edit", command=self.edit_book)# type: ignore
        self.deleteButton = ttk.Button(self, text="Delete", command=self.delete_book)# type: ignore
        self.clearButton = ttk.Button(self, text="Clear", command=self.clear_fields)# type: ignore
        self.exitButton = ttk.Button(self, text="Exit", command=self.quit)

        self.label1.grid(row=0, column=0, sticky=tk.W)
        self.textField1.grid(row=0, column=1)
        self.label2.grid(row=1, column=0, sticky=tk.W)
        self.textField2.grid(row=1, column=1)
        self.label3.grid(row=2, column=0, sticky=tk.W)
        self.textField3.grid(row=2, column=1)
        self.label4.grid(row=3, column=0, sticky=tk.W)
        self.textField4.grid(row=3, column=1)
        self.label5.grid(row=4, column=0, sticky=tk.W)
        self.textField5.grid(row=4, column=1)
        self.label6.grid(row=5, column=0, sticky=tk.W)
        self.textField6.grid(row=5, column=1)
        self.label7.grid(row=6, column=0, sticky=tk.W)
        self.textField7.grid(row=6, column=1)
        self.addButton.grid(row=7, column=0)
        self.viewButton.grid(row=7, column=1)
        self.editButton.grid(row=8, column=0)
        self.deleteButton.grid(row=8, column=1)
        self.clearButton.grid(row=9, column=0)
        self.exitButton.grid(row=9, column=1)

        self.books = []

    def add_book(self):
        book = [
            self.textField1.get(),
            self.textField2.get(),
            self.textField3.get(),
            self.textField4.get(),
            self.textField5.get(),
            self.textField6.get(),
            self.textField7.get()
        ]
        self.books.append(book)
        messagebox.showinfo("Success", "Book added successfully")
        self.clear_fields() # type: ignore

    def view_books(self):
        columns = ["Book ID", "Book Title", "Author", "Publisher"]
