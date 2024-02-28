import tkinter as tk
from tkinter import messagebox
import customtkinter

def run_other_code():
    our_bag = [
        [10, 1.99, 'Apple'],
        [0, 2.20, 'Banana'],
        [10, 1.50, 'Orange'],
        [10, 2.00, 'Mango'],
        [10, 1.70, 'Kiwi'],
    ]

    user_bag = []

    def print_menu():
        menu_text = "Available Products:\n"
        for i in range(len(our_bag)):
            if our_bag[i][0] > 0:
                menu_text += f"{our_bag[i][2]} - {our_bag[i][1]:.2f}€\n"
        menu_text += "Exit - done."
        return menu_text
    
    def get_index_by_product():
        product = string_entry.get().lower()
        for i in range(len(our_bag)):
            if our_bag[i][2].lower() == product:
                return i
        return -1

    def show_input_dialog():
        try:
            user_integer = int(integer_quantity.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return None

        index = get_index_by_product()
        user_integer_for_if = user_integer
        if index == -1:
            messagebox.showerror("Error", "Product not found.")
            return None
        if index != -1 and our_bag[index][0] >= user_integer_for_if:
            user_string = string_entry.get().lower()
            price = find_price_for_item(index)
            add_to_user_bag(user_string, user_integer, price)
            to_remove(index, user_integer)
            print(user_bag)
            print(our_bag)

        # Clear the input fields
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)
            return user_string, user_integer, price
        elif our_bag[index][0] <= user_integer_for_if:
            messagebox.showerror("Out of Stock","We don't have enough in stock.")
            string_entry.delete(0, tk.END)
            integer_quantity.delete(0, tk.END)


    def done():
        total = sum(user[2] for user in user_bag)
        receipt_or_no = messagebox.askyesno("Receipt", "Do you want a receipt?")

        if receipt_or_no:
            print_bill(total)
            user_bag.clear()
            root.destroy()
            
        else:
            messagebox.showinfo("Total", f"Total: {total:.2f}€")
            user_bag.clear()
            root.destroy()

    def add_to_user_bag(product, quantity, price):
        price1 = price * quantity
        user_bag.append([product, quantity, price1])

    def to_remove(index, quantity):
        our_bag[index][0] -= quantity

    def find_price_for_item(index):
        return our_bag[index][1]

    def print_bill(total):
        receipt = "\nReceipt:\n----------------------------\n"
        for user in user_bag:
            name, quantity, price = user
            receipt += f"{name} - {price:.2f}€ x {quantity}\n"
        receipt += "----------------------------\n"
        receipt += f"Total: {total:.2f}€\n"
        receipt += "Thank you for shopping!"
        messagebox.showinfo("Receipt", receipt)

    root = customtkinter.CTk()
    root.title("Input Example")
    root.geometry("500x600")

    # Left side: Print Menu
    menu_label = customtkinter.CTkLabel(root, text=print_menu(), justify=tk.LEFT)
    menu_label.pack(side=tk.LEFT, padx=20, pady=20)

    # Right side: Input Fields
    input_frame = customtkinter.CTkFrame(root)
    input_frame.pack(side=tk.RIGHT, padx=20, pady=20)
    
    string_entry_label = customtkinter.CTkLabel(input_frame, text="Enter the product:")
    string_entry_label.pack()

    string_entry = customtkinter.CTkEntry(input_frame)
    string_entry.pack(pady=10)

    integer_label = customtkinter.CTkLabel(input_frame, text="Enter how many you want to buy:")
    integer_label.pack()

    integer_quantity = customtkinter.CTkEntry(input_frame)
    integer_quantity.pack(pady=10)

    # Button below the input frame
    button = customtkinter.CTkButton(root, text="Next", command=show_input_dialog)
    button.pack(side=tk.BOTTOM, pady=10)

    button_exit = customtkinter.CTkButton(root, text="Done", command=done)
    button_exit.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()


