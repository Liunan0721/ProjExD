import tkinter as tk
import maze_maker as mm
import time

def key_down(event):
    global key
    key = event.keysym
    print(key)


def key_up(event):
    global key
    key = ""


def resert():
    global mx, my, st
    st = time.time()
    mx, my =1, 1
    

def main_proc():
    global cx, cy, mx, my, kokaton, ed
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if key == "r": # キーrを押すと
        resert()
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        if key == "Up":my += 1
        if key == "Down":my -= 1
        if key == "Left":mx += 1
        if key == "Right":mx -= 1
    if cx == 13*100+50 and cy == 7*100+50:    #こうかとんが終点に到達したら
        kokaton = tk.PhotoImage(file="fig/6.png")
        canvas.create_image(cx, cy, image=kokaton, tag="kokaton")
        ed = time.time()
        label = tk.Label(root, text=f"所要時間：{(ed-st):.2f}秒", font=("", 30))
        label.pack()
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)

    mx, my =1, 1
    cx, cy = mx*100+50, my*100+50
    kokaton = tk.PhotoImage(file="fig/4.png")
    canvas.create_image(cx, cy, image=kokaton, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    st = time.time()
    ed = 0

    root.mainloop()