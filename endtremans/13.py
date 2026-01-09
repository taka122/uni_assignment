char = (input("文字列"))
# result = 0
result = ""
for n in char:  
    if n.isdigit():    
        result += n
print(result)