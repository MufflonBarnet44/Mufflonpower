import tkinter as tk

def change_text():
    label.config(text="You clicked me")


# Create the manin window
root = tk.Tk()
label = tk.Label(root, text="Hello")
label.pack(pady= 20)

button = tk.Button(root, text="Click me", command=change_text)
button.pack()

root.mainloop()