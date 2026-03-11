import tkinter as tk

root = tk.Tk()
root.title("Загрузка")
root.geometry("500x180")
root.configure(bg="white")

label = tk.Label(root, text="Загрузка файлов…", font=("Verdana", 24), fg="#333333", bg="white")
label.pack(pady=20)

outer_frame = tk.Frame(root, width=400, height=40, bg="#E0E0E0", bd=1, relief="solid")
outer_frame.pack()

inner_frame = tk.Frame(outer_frame, width=240, height=36, bg="#00BFFF")
inner_frame.pack(side=tk.LEFT, pady=2)

root.mainloop()