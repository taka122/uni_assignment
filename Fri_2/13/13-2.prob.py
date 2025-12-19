# じゃんけんゲームプログラムの空欄を埋めよ．実行例は以下の通りである．
import random

hand = ["グー","チョキ","パー"]
print("じゃんけんしましょう！")
while True:
    # com = random.
    print("******")
    for i, desc in enumerate(hand):
        print(i, ":", desc)
    you = int(input("出す手を数値で入力："))
    if you < 0 or you > 2:
        print("0から2の間で入力してね")
        continue
    print("---")
    # print("自分：", )
    # print("相手：", )
    print("---")
    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("あなたの負け！")
    else:
        print("あなたの勝ち！")
    print("---")

# % python3 janken.py
# じゃんけんしましょう！
# ******
# 0 : グー
# 1 : チョキ
# 2 : パー
# 出す手を数値で入力：0
# ---
# 自分： グー
# 相手： チョキ
# ---
# あなたの勝ち！
# ---
# ******
