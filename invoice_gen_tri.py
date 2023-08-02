import tkinter as tk
from tkinter import ttk, messagebox
from docxtpl import DocxTemplate
import datetime

class InvoiceGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Generator Form")
        self.invoice_list = []
        self.initialize_gui()

    def initialize_gui(self):
        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=10)

        first_name_label = ttk.Label(frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = ttk.Label(frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        self.first_name_entry = ttk.Entry(frame)
        self.last_name_entry = ttk.Entry(frame)
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)

        phone_label = ttk.Label(frame, text="Phone")
        phone_label.grid(row=0, column=2)
        self.phone_entry = ttk.Entry(frame)
        self.phone_entry.grid(row=1, column=2)

        qty_label = ttk.Label(frame, text="Qty")
        qty_label.grid(row=2, column=0)
        self.qty_spinbox = ttk.Spinbox(frame, from_=1, to=100)
        self.qty_spinbox.grid(row=3, column=0)

        desc_label = ttk.Label(frame, text="Description")
        desc_label.grid(row=2, column=1)
        self.desc_entry = ttk.Entry(frame)
        self.desc_entry.grid(row=3, column=1)

        price_label = ttk.Label(frame, text="Unit Price")
        price_label.grid(row=2, column=2)
        self.price_spinbox = ttk.Spinbox(frame, from_=0.0, to=500, increment=0.5)
        self.price_spinbox.grid(row=3, column=2)

        add_item_button = ttk.Button(frame, text="Add Item", command=self.add_item)
        add_item_button.grid(row=4, column=2, pady=5)

        columns = ('qty', 'desc', 'price', 'total')
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        self.tree.heading('qty', text='Qty')
        self.tree.heading('desc', text='Description')
        self.tree.heading('price', text='Unit Price')
        self.tree.heading('total', text="Total")
        self.tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

        save_invoice_button = ttk.Button(frame, text="Generate Invoice", command=self.generate_invoice)
        save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)

        new_invoice_button = ttk.Button(frame, text="New Invoice", command=self.new_invoice)
        new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)

    def clear_item(self):
        self.qty_spinbox.delete(0, tk.END)
        self.qty_spinbox.insert(0, "1")
        self.desc_entry.delete(0, tk.END)
        self.price_spinbox.delete(0, tk.END)
        self.price_spinbox.insert(0, "0.0")

    def add_item(self):
        qty = int(self.qty_spinbox.get())
        desc = self.desc_entry.get()
        price = float(self.price_spinbox.get())

        if not desc or price <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a valid description and price.")
            return

        line_total = qty * price
        invoice_item = [qty, desc, price, line_total]
        self.tree.insert('', 0, values=invoice_item)
        self.clear_item()
        self.invoice_list.append(invoice_item)

    def new_invoice(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.clear_item()
        self.tree.delete(*self.tree.get_children())
        self.invoice_list.clear()

    def generate_invoice(self):
        if not self.invoice_list:
            messagebox.showwarning("Empty Invoice", "Cannot generate an empty invoice.")
            return

        doc = DocxTemplate("invoice_template.docx")
        name = self.first_name_entry.get() + " " + self.last_name_entry.get()
        phone = self.phone_entry.get()
        subtotal = sum(item[3] for item in self.invoice_list)
        salestax = 0.1
        total = subtotal * (1 + salestax)

        doc.render({"name": name,
                    "phone": phone,
                    "invoice_list": self.invoice_list,
                    "subtotal": subtotal,
                    "salestax": str(salestax * 100) + "%",
                    "total": total})

        doc_name = f"new_invoice_{name}_{datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')}.docx"
        doc.save(doc_name)

        messagebox.showinfo("Invoice Complete", "Invoice generated successfully.")
        self.new_invoice()

if __name__ == "__main__":
    app = InvoiceGenerator()
    app.mainloop()
