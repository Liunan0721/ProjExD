import tkinter as tk

#練習
root = tk.Tk()
root.title("tk")
root.geometry("300x500")

#練習2
r, c = 0, 0
for num in range(9, -1, -1):
    for i in range(3):
        button9 = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
        button9.grid(row= r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()