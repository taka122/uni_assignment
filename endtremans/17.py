class student: 
    def   __init__(self, name , id):   
       self. name = name  
       self. id   = id
    def change_name (self, new_name):
        self.name = new_name
name = str(input("name"))
id   = int(input("id"))
s = student(name,id)
print (f"{s.name},{s.id}")

new_name = input ("Enter new name: ")
s.change_name(new_name)
print (f"{s.name},{s.id}")