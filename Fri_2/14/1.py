# 一つだけ与えた引数を表示するプログラムを，引数が無い場合の例外処理を加えて作成せよ



# 【実行例】

# % python3 quiz_exception.py XYZ

# XYZ

# % python3 quiz_exception.py

# No arguments



# (入力必須)

import sys

try:
    print(sys.argv[1])
except IndexError:
    print("No arguments")

 