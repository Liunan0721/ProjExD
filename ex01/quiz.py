import random
import time

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題：" + qa["q"])
    return qa["a"]

def kaitou(ans_lst):
    st = time.time()
    ans =  input("答えるんだ：")
    ed = time.time()
    if ans in ans_lst:
        print("正解!!!")
    else:
        print("出直してこい")
    
    print(f"所要時間：{(ed-st):.2f}秒")


if __name__ == "__main__":
    qa_lst = [
        {"q":"プロジェクト演習テーマDの講義はどこでやっているか?", "a":["研究棟A教室303", "研究棟A", "研A303"]},
        {"q":"テーマDは何のプログラミング言語を使って作業するか?", "a":["Python", "python"]},
        {"q":"プロジェクト演習テーマDの担当教員は誰ですか?", "a":["伏見先生", "伏見卓恭","伏見"]}
    ]

    ans_lst = shutudai(qa_lst)
    kaitou(ans_lst)
