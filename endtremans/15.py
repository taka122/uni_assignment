alphabets = {"A": 12, "B": 23, "C": 34, "D": 45}
def heal (a): 
     for key, value in a.items(): 
           a[key] += 10  
     return a
result = heal(alphabets)
for value in result.items(): 
     print(value)     