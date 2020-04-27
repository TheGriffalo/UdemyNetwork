x = 10

if x < 10:
	for i in range(1, 5):
		print(x * i)
elif x > 10:
	j = 1
	while j < 5:
		print(x * j)
		j = j + 1
else:
	print(x ** 10)