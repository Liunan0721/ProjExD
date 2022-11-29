import tkinter as tk
import tkinter.messagebox as tkm

#練習1
root = tk.Tk()
root.title("tk")
root.geometry("300x500")

#練習3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("", f"{num}ボタンがクリックされました")

#練習2
r, c = 0, 0
for num in range(9, -1, -1):
    for i in range(3):
        button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
        button.grid(row= r, column=c)
        button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()