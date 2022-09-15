# In this kata you are required to, given a string,
# replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	index = 0
	result = ""
	text = text.casefold()
	for char in text:
		index = alphabets.find(char) + 1
		if (result):
			result += " "
		if (index > 0):
			result += (str)(index)
	print(result)
	return result

alphabet_position("The sunset sets at twelve o' clock.")
