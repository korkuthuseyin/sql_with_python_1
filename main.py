import lib
import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("Add Product")
# Set the window size
window.geometry("800x600")
# add two textboxes
product_name = tk.Entry(window)
product_name.pack()
product_barcode = tk.Entry(window)
product_barcode.pack()

# add a button
def add_product():
    name = product_name.get()
    barcode = product_barcode.get()
    lib.insert_data('products', name, barcode)
    product_name.delete(0, 'end')
    product_barcode.delete(0, 'end')

add_button = tk.Button(window, text="Add Product", command=add_product, justify='center')
add_button.pack()

# textboxes and button should center
window.update_idletasks()
add_button.place(x=window.winfo_width()//2 - add_button.winfo_width()//2, y=window.winfo_height()//2 - add_button.winfo_height()//2)
product_name.place(x=window.winfo_width()//2 - product_name.winfo_width()//2, y=window.winfo_height()//2 - product_name.winfo_height()//2 - 50)
product_barcode.place(x=window.winfo_width()//2 - product_barcode.winfo_width()//2, y=window.winfo_height()//2 - product_barcode.winfo_height()//2 - 100)

# add texts in front of textboxes
product_name_label = tk.Label(window, text="Product Name: ")
product_name_label.pack()
product_barcode_label = tk.Label(window, text="Product Barcode: ")
product_barcode_label.pack()

# textboxes should be on the right of labels
window.update_idletasks()
product_name_label.place(x=window.winfo_width()//2 - product_name.winfo_width()//2 - 120, y=window.winfo_height()//2 - product_name.winfo_height()//2 - 50)
product_barcode_label.place(x=window.winfo_width()//2 - product_barcode.winfo_width()//2 - 120, y=window.winfo_height()//2 - product_barcode.winfo_height()//2 - 100)


# Run the main loop
window.mainloop()