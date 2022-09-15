# Your code must return true or false (not 'true' and 'false')
# depending upon whether the given number is a Narcissistic number in base 10.
# This may be True and False in your language, e.g. PHP.

def narcissistic( value ):
	original_value = value
	result = 0
	number_str = str(value)
	if value == 0:
		digit_count = 1
	else:
		digit_count = 0
	while value != 0:
		value = int(value / 10)
		digit_count += 1
	for digit in number_str:
		result += int(digit) ** digit_count
	if result == original_value:
		return True
	return False