import tkinter as tk

root = tk.Tk()
root.title("Профиль")
root.geometry("400x500")
root.configure(bg="#F0F4F8")

name_label = tk.Label(root, text="Александр Иванов", font=("Georgia", 32, "bold"), fg="#1A3C5A", bg="#F0F4F8")
name_label.pack(pady=(30, 0))

handle_label = tk.Label(root, text="@sasha_code", font=("Courier", 18), fg="#666666", bg="#F0F4F8")
handle_label.pack()

frame = tk.Frame(root, width=300, height=180, bg="white", bd=2, relief="solid")
frame.pack(pady=20)

dev_label = tk.Label(frame, text="Python Developer", font=("Arial", 20, "bold"), fg="#2E8B57", bg="white")
dev_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()