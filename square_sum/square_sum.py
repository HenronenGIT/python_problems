def square_sum(numbers):
	i = 0
	result = 0
	for number in numbers:
		result += number * number
	return (result)

square_sum([1,2])
square_sum([0, 3, 4, 5])
square_sum([])
square_sum([-1,-2])
square_sum([-1,0,1])
