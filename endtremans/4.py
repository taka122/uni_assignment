numbers={"いち":1,"に":2,"さん":3,"し":4,"ご":5}
for key, value in numbers.items():
	if value % 2 == 0:
		print(f" {key} {value}偶数")
	else:
		print(f" {key} {value}")

