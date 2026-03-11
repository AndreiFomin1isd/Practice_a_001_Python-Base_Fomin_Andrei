import tkinter as tk

root = tk.Tk()
root.title("Три блока")
root.geometry("600x300")
root.configure(bg="white")

frame1 = tk.Frame(root, width=180, height=260, bg="#FF4040")
frame1.pack(side=tk.LEFT, padx=10, pady=20)

frame2 = tk.Frame(root, width=180, height=260, bg="#4040FF")
frame2.pack(side=tk.LEFT, padx=10, pady=20)

frame3 = tk.Frame(root, width=180, height=260, bg="#40FF40")
frame3.pack(side=tk.LEFT, padx=10, pady=20)

label1 = tk.Label(frame1, text="Красный", font=("Arial", 28, "bold"), fg="white", bg="#FF4040")
label1.place(relx=0.5, rely=0.5, anchor="center")

label2 = tk.Label(frame2, text="Синий", font=("Arial", 28, "bold"), fg="white", bg="#4040FF")
label2.place(relx=0.5, rely=0.5, anchor="center")

label3 = tk.Label(frame3, text="Зелёный", font=("Arial", 28, "bold"), fg="white", bg="#40FF40")
label3.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()