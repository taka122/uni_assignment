class Student:
	def __init__(self, name, id):
		self. name = name
		self. id = id
	def change_name(self, new_name):
		self. name = new_name
name = input("文字列：")
id = int(input ("id:"))
taro = Student (name, id)
print (f" {taro.name} {taro.id}")

new_name = input("新しい名前：")
taro.change_name(new_name)
print (f" {taro.name} {taro.id}")