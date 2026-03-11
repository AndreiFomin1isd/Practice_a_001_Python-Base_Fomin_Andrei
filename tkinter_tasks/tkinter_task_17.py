import tkinter as tk

root = tk.Tk()
root.title("Действие")
root.geometry("360x240")
root.configure(bg="#E8F5E9")

blank_image = tk.PhotoImage(width=280, height=80)

button = tk.Button(root, text="НАЧАТЬ ИГРУ", image=blank_image, compound="center",
                   font=("Arial", 28, "bold"), fg="white", bg="#4CAF50",
                   relief="raised", bd=6)
button.place(relx=0.5, rely=0.5, anchor="center")
button.image = blank_image  # Keep reference

root.mainloop()