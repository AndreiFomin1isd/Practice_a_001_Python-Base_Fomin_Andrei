import tkinter as tk

root = tk.Tk()
root.title("Моё яркое приветствие")
root.geometry("500x200")
root.configure(bg="#FFFACD")

label1 = tk.Label(root, text="HELLO WORLD!", font=("Impact", 48, "bold"), fg="#800080")
label1.pack(pady=10)

label2 = tk.Label(root, text="Это мой первый яркий текст", font=("Comic Sans MS", 24, "italic"), fg="#C71585")
label2.pack()

root.mainloop()