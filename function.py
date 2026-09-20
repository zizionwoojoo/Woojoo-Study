def find_max(numbers):    
	big = numbers[0]


	for i in range(0, len(numbers)):
        	if (big > numbers[i]):
                	continue
        	elif (big < numbers[i]):
        	        big = numbers[i]  
	return big

number = [10, 20, 31, 76, 2, 83, 91, 5]
result = find_max(number)
print("가장 큰수는", result, "입니다.")

	
