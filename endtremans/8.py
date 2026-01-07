class Student:
	def __init__(self, name, id):
		self.name = name
		self.id = id
	def change_name(self, new_name):
		self.name = new_name
name = input("文字列：")
id = int(input ("id:"))
s = Student (name, id)
print (f" {s.name} {s.id}")

new_name = input("新しい名前：")
s.change_name(new_name)
print (f"{s.name} {s.id}")