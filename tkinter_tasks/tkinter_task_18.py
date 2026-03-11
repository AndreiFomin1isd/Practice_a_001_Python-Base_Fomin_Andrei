import tkinter as tk

root = tk.Tk()
root.title("Результат")
root.geometry("420x260")
root.configure(bg="white")

canvas = tk.Canvas(root, width=400, height=120, bg="white", highlightthickness=0)
canvas.pack(pady=(30, 0))

canvas.create_oval(5, 5, 395, 115, fill="#228B22")
canvas.create_text(200, 60, text="ГОТОВО!", font=("Impact", 60), fill="white")

label = tk.Label(root, text="Ваши данные успешно сохранены", font=("Arial", 18), fg="#555555", bg="white")
label.pack(pady=20)

root.mainloop()