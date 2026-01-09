answer = int(input("ゲームを再開しますか？はい->1、いいえ->0："))

if answer == 1:
    print("セーブファイルは以下の通りです。save11.txt, save12.txt, save13.txt")
    filename = input("再開するファイル名を入力してください：")
    with open(filename, "r") as f:
        location = f.read()
    print(f"{location}からゲームを再開します。")
elif answer == 0:
    print("ゲームの再開をキャンセルしました。")
