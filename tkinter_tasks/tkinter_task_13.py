import tkinter as tk

root = tk.Tk()
root.title("Меню")
root.geometry("280x420")
root.configure(bg="#2F2F2F")

blank_image = tk.PhotoImage(width=220, height=50)

button_frame = tk.Frame(root, bg="#2F2F2F")
button_frame.place(relx=0.5, rely=0.5, anchor="center")

texts = ["Главная", "Профиль", "Друзья", "Сообщения", "Настройки"]

for text in texts:
    button = tk.Button(button_frame, text=text, image=blank_image, compound="center",
                       font=("Arial", 16, "bold"), fg="white", bg="#4A4A4A")
    button.pack(side=tk.TOP)
    button.image = blank_image  # Keep reference

root.mainloop()