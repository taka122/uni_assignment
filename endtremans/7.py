class Student:
	def __init__ (self, name, id):
		self.name = name
		self.id = id
name = input("文字列：")
id = int(input ("id:"))
taro = Student (name, id)
print(f" {taro.name} {taro.id}")