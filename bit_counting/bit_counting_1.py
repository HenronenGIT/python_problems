# Write a function that takes an integer as input,
# and returns the number of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):

	one_count = 0
	bits = ""
	if (n == 0):
		bits = "0"
	else:
		while (n != 0):
			bits += (str)((int)(n % 2))
			n = (int)(n / 2)
	for ch in bits:
		if (ch == '1'):
			one_count += 1
	return (one_count)

assert count_bits(0) == 0
assert count_bits(4) == 1
assert count_bits(7) == 3
assert count_bits(9) == 2
assert count_bits(10) == 2