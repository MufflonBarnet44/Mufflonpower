import tkinter as tk

# Create the manin window
root = tk.Tk()
root.title("Greeting")

label = tk.Label(root, text="Hello, Tkinter")
label.pack(pady= 20)

root.mainloop()