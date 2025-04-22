import tkinter as tk

root= tk.Tk()
root.title("Basic Ui Demo")
root.geometry("300x350")
 
label = tk.Label(root, text="This is a label")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=10)

