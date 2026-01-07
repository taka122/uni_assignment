

# 四則演算のまとめ（Python）

- 加算: `a + b`
- 減算: `a - b`
- 乗算: `a * b`
- 除算（実数）: `a / b`（結果は常に float）
- 余り: `a % b`
- 整数除算: `a // b`
- 累乗: `a ** b`
- 優先順位: `()` → `**` → `* / // %` → `+ -`
- 代入付き演算: `+= -= *= /= //= %= **=`
- 型の注意: `int` と `float` が混ざると結果は `float`

# range の指定方法（Python）

- `range(stop)`：0 から `stop-1` まで
- `range(start, stop)`：`start` から `stop-1` まで
- `range(start, stop, step)`：`start` から `stop-1` まで `step` ずつ進む

# 文字列メソッド isdigit

- 形式: `文字列.isdigit()`
- 意味: 文字列が数字だけで構成されていれば True、それ以外は False

# ファイル書き込みと乱数

- `import random`：乱数モジュールを使う
- `random.randint(1, 100)`：1〜100の整数乱数を1つ生成
- `[... for _ in range(10)]`：リスト内包表記で10個の値を作る
- `with open("tmp.txt", "w") as file`：書き込み用に開き、ブロック終了で自動クローズ
- `file.write(f" {number}\n")`：1行ずつ書き込み（先頭に空白＋改行）

# リスト内包表記

- 形式: `[式 for 変数 in イテラブル]`
- 意味: イテラブルを回して式の結果をリストにする
- 例: `[random.randint(1, 100) for n in range(10)]`

# クラスの基本

- 定義: `class クラス名:`
- 初期化: `def __init__(self, ...):` で属性を設定する
- メソッド: `def メソッド名(self, ...):` でインスタンス操作
- インスタンス生成: `obj = クラス名(引数)`
- 属性アクセス: `obj.属性名`

# 入力と型変換

- `input("...")`：文字列として入力を受け取る
- `int(...)`：文字列を整数に変換する

# f-string

- 形式: `f"{変数}"`
- 意味: 変数の値を文字列内に埋め込む

# クラス内の文法（self とメソッド）

- `class Student:`：クラス定義
- `def __init__(self, name, id):`：コンストラクタ（インスタンス生成時に呼ばれる）
- `self`：そのインスタンス自身を指す
- `self.name = name`：インスタンス変数（属性）の代入
- `def change_name(self, new_name):`：インスタンスメソッドの定義
