import tkinter as tk
from tkinter import messagebox
import customtkinter

our_bag = [
    [10, 1.99, "Apple"],
    [0, 2.20, "Banana"],
    [10, 1.50, "Orange"],
    [10, 2.00, "Mango"],
    [10, 1.70, "Kiwi"],
]

def get_index_by_product(product):
    if product is not None:
        product = product.lower()
        for i in range(len(our_bag)):
            if our_bag[i][2].lower() == product:
                return i
    return -1

def print_stock():
    menu_text = "Available Products:\n"
    for i in range(len(our_bag)):
        menu_text += f"{our_bag[i][2]} - {our_bag[i][0]}\n"
    menu_text += "Exit - done."
    return menu_text

def restock_items():
    def done():
        root.destroy()

    def restock():
        product = string_entry.get().lower()
        index = get_index_by_product(product)
        if index != -1:
            price = int(integer_quantity.get())
            our_bag[index][0] += price
            messagebox.showinfo("Stock", f" The total stock of {product} is now {our_bag[index][0]}.")
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)
            return product, price
        else:
            messagebox.showwarning("Product Not Found", f"{product} not found in the inventory.")
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)
    
    root = customtkinter.CTk()
    root.title("Restock Items")
    root.geometry("500x600")

    menu_label = customtkinter.CTkLabel(root, text=print_stock(), justify=tk.LEFT)
    menu_label.pack(side=tk.LEFT, padx=20, pady=20)

    input_frame = customtkinter.CTkFrame(root)
    input_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    string_entry_label = customtkinter.CTkLabel(input_frame, text="Enter the product:")
    string_entry_label.pack()

    string_entry = customtkinter.CTkEntry(input_frame)
    string_entry.pack(pady=10)

    integer_label = customtkinter.CTkLabel(input_frame, text="Enter how many you want to add:")
    integer_label.pack()

    integer_quantity = customtkinter.CTkEntry(input_frame)
    integer_quantity.pack(pady=10)

    # Button below the input frame
    button = customtkinter.CTkButton(root, text="Next", command=restock)
    button.pack(side=tk.BOTTOM, pady=10)

    button_exit = customtkinter.CTkButton(root, text="Done", command=done)
    button_exit.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

def change_price():
    def print_menu():
        menu_text = "Available Products:\n"
        for i in range(len(our_bag)):
            if our_bag[i][0] > 0:
                menu_text += f"{our_bag[i][2]} - {our_bag[i][1]:.2f}€\n"
        menu_text += "Exit - done."
        return menu_text
    def done():
        root.destroy()

    def change():
        product = string_entry.get().lower()
        index = get_index_by_product(product)
        if index != -1:
            new_price = int(integer_quantity.get())
            our_bag[index][1] = new_price
            messagebox.showinfo("Price Change", f"Price of {product} updated to {new_price}")
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)
        else:
            messagebox.showwarning("Product Not Found", f"{product} not found in the inventory.")
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)
    
    root = customtkinter.CTk()
    root.title("Change Price")
    root.geometry("400x600")

    menu_label = customtkinter.CTkLabel(root, text=print_menu(), justify=tk.LEFT)
    menu_label.pack(side=tk.LEFT, padx=20, pady=20)

    input_frame = customtkinter.CTkFrame(root)
    input_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    string_entry_label = customtkinter.CTkLabel(input_frame, text="Enter the product:")
    string_entry_label.pack()

    string_entry = customtkinter.CTkEntry(input_frame)
    string_entry.pack(pady=10)

    integer_label = customtkinter.CTkLabel(input_frame, text="Enter your new price:")
    integer_label.pack()

    integer_quantity = customtkinter.CTkEntry(input_frame)
    integer_quantity.pack(pady=10)

    # Button below the input frame
    button = customtkinter.CTkButton(root, text="Next", command=change)
    button.pack(side=tk.BOTTOM, pady=10)

    button_exit = customtkinter.CTkButton(root, text="Done", command=done)
    button_exit.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()
