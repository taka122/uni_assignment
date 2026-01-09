import random
with open ("tmp.txt", "w") as file :
    random_num = (random.randint(1,100)for i in range(10)) 
    for num in random_num :
        file.write(f"{num}\n")