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

    elif num in function:
        siki = entry.get()
        if num == "C":
            entry.delete(0, tk.END) 
        
        if num == "←":
            entry.delete(len(siki)-1, tk.END) # 表示文字列の一桁を消す

        if num == "x^2":
            siki = entry.get()
            res = float(siki)**2
            entry.delete(0,tk.END)
            entry.insert(tk.END, res)

        if num == "1/x":
            siki = entry.get()
            res = 1/float(siki)
            entry.delete(0,tk.END)
            entry.insert(tk.END, res)




    else: #[=]とclearリスト以外の文字列
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        #練習6

        entry.insert(tk.END, num)



#練習1
root = tk.Tk()
root.title("tk")
root.geometry("300x500")


#練習4
entry  = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)


r, c = 1, 0
function = ["%", "CE", "C", "←", "1/x", "x^2", "√x"]
for fun in function:
    button = tk.Button(root, text=f"{fun}", width=3, height=1, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c % 4 == 0:
        r+=1
        c=0


#練習2
r, c = 3, 2
for num in range(9, -1, -1):
    if num == 0:
        r, c = 6, 0
    button = tk.Button(root, text=f"{num}", width=3, height=1, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    c -= 1
    if c == -1:
        r += 1
        c = 2
button = tk.Button(root, text=".", width=3, height=1, font=("", 30))
button.grid(row= 6, column=1)
button.bind("<1>", button_click)
    



#練習5
r, c = 2, 3
operators = ["+", "-", "*", "/", "="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=3, height=1, font=("", 30))
    button.grid(row= r, column=c)
    button.bind("<1>", button_click)
    r += 1





root.mainloop()