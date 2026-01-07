import random
with open ("tmp.txt", "w") as file:
	random_numbers = [random.randint(1, 100) for n in range (10)]
	for number in random_numbers:
	 file.write(f" {number}\n")
