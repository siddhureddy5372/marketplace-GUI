import customtkinter
import tkinter
from tkinter import simpledialog, messagebox

# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("red")
import anotherGUI
import ownerGUI


def button_click():
    app.destroy()
    anotherGUI.run_other_code()


def button_owner_click():
    product_name1 = simpledialog.askstring("Input", " 'Restock' or 'Change price': ")
    product_name = product_name1.strip().lower() 
    if product_name == "restock":
        app.destroy()
        ownerGUI.restock_items()
    elif product_name == "change price":
        app.destroy()
        ownerGUI.change_price()
    elif product_name != "restock" and product_name.lower() != "change price":
        messagebox.showerror("Invalid answer", "It is not an option.")


app = customtkinter.CTk()
app.title("Siddhu")
app.geometry("500x600")

frame = customtkinter.CTkFrame(master=app, width=200, height=200, corner_radius=10)
frame.pack(padx=20, pady=20)
label = customtkinter.CTkLabel(
    master=frame,
    text="MarketPlace",
    width=120,
    height=30,
    fg_color=("white", "red"),
    corner_radius=8,
)

label.grid(padx=20, pady=10)
button = customtkinter.CTkButton(app, text="User", command=button_click)
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
button_owner = customtkinter.CTkButton(app, text="Owner", command=button_owner_click)
button_owner.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
app.mainloop()
