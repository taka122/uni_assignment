
# 2025-12-19 (Fri)
# 田中　貴久 | 設定 | ログアウト
# マイページコースお知らせポートフォリオ
# 53261:プログラミング言語(C1) シラバス小テストアンケートレポートプロジェクト成績(採点結果)1掲示板コンテンツ(教材)
# 2025 秋セメスター:秋セメ・金2(3-4)
# 金2:H802 / 服部 宏充
# 提出完了

#  SSD_プロ言_2025_L13_Q00
# 課題に関する説明	
# 制限時間	5分間
# 制限時間内のみ回答可
# 受付開始日時	2025-12-19 11:27:14
# 受付終了日時	未設定
# Submit
# ポートフォリオ	回答を提出者のポートフォリオに追加
# 採点結果と解説の公開	公開しない
# 状態	受付中
# 提出済み
# 提出した回答（提出日時：2025-12-19 11:31）
# 回答数 1 / 1 経過時間 00:04:37 残り時間 00:00:23
# inheritance.pyから，別ファイル上のstudents_m.pyのクラスを利用するために，以下の空白を埋めよ．
# students_m.py
class Student:
    def __init__(self, id, name, score = 0):
        self.id = id
        self.name = name
        self.score = score
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score = score
class CalcScore:
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        self.students.append(student)
    def ave(self):
        total = 0
        for st in self.students:
            total += st.getScore()
        ave = total / len(self.students)
        return ave
# inheritance.py
# (入力必須)
from students_m import Student, CalcScor
 
class NeoCalcScore(CalcScore):
    def maxScore(self):
        max = 0
        for st in self.students:
            if (max <= st.getScore()):
                max = st.getScore()
        return # 学生を表すインスタンスを作成
p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "田中", score = 84)
p4 = Student(13, "山田", score = 77)
# 平均点・最低点を計算
calc = NeoCalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点=", calc.ave())
print("最高点=", calc.maxScore())