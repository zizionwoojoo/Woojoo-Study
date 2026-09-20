number = [2, 4, 7, 9, 10, 15]
big = number[0]


for i in range(0, len(number)):
	if (big > number[i]):
		continue
	elif (big < number[i]):
		big = number[i]
print("가장 큰수는", big, "입니다.")

