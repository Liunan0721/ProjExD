import random;
import datetime

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題：" + qa["q"])
    return qa["a"]

def kaitou(ans_lst):
    st = datetime.datetime.now()
    ans =  input("答えるんだ：")
    ed = datetime.datetime.now()
    if ans in ans_lst:
        print("正解!!!")
    else:
        print("出直してこい")
    print("回答時間：" + (ed - st).seconds)


if __name__ == "__main__":
    qa_lst = [
        {"q":"プロジェクト演習テーマDの講義はどこでやっているか?", "a":["研究棟A教室303", "研究棟A", "研A303"]},
        {"q":"問題2", "a":["1", "2"]},
        {"q":"問題3", "a":["1", "2"]}
    ]

    ans_lst = shutudai(qa_lst)
    kaitou(ans_lst)
