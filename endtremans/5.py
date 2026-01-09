def heal(a):
	for key in a:
		a[key] += 10
	return a
alphabets = {"A": 12, "B": 23, "C": 34, "D": 45}
updated_alphabets = heal(alphabets)
print(f"{updated_alphabets}")
print(f"{updated_alphabets.items()}")

for key, value in updated_alphabets.items():
	print(f"{key} {value}")