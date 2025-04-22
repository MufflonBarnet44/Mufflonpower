import tkinter as tk

# Create the manin window
root = tk.Tk()
root.title("Basic GUI window")
root.geometry("300x350")

# Label
label = tk.Label(root, text="This is a lable")
label.pack(pady=10)

# Entry Box
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button= tk.Button(root, text="Click me")
button.pack(pady=5)

# Ralio buttons

radio1 = tk.Radiobutton(root, text="Opton 1", value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Opton 2", value=2)
radio2.pack()

#checkbox
checkbox = tk.Checkbutton(root, text= "Börja Prenunmerera")
checkbox.pack(pady=5)

# Dropdown meny
options = ["java","python","c++"]
dropdown_var = tk.StringVar(value=options[0])
                            
dropdown_label = tk.Label(root, text="favorit språk")      
dropdown_label.pack(pady=(10, 0))

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

root.mainloop()