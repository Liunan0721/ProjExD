import tkinter as tk
import tkinter.messagebox as tkm


#練習3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        #練習7
        siki = entry.get() # 数式の文字列を取得する
        res = eval(siki) # 数式文字列を評価する
        entry.delete(0, tk.END) # 表示文字列の削除
        entry.insert(tk.END, res) # 結果の挿入
        
    else: #[=]以外の文字列
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        #練習6
        entry.insert(tk.END, num)

#練習1
root = tk.Tk()
root.title("tk")
root.geometry("300x500")


#練習4
entry  = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=3)


#練習2
r, c = 1, 0
for num in range(9, -1, -1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0


#練習5
operators = ["+", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()