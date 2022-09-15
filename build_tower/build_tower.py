# Build Tower
# Build a pyramid-shaped tower given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]

def tower_builder(n_floors):
	stars = ""
	space = ""
	result = []
	i = 1
	while (i <= n_floors):
		stars = '*' * (2 * i - 1)
		space = ' ' * (n_floors - i)
		result.append(space + stars + space)
		i += 1
	return (result)

tower_builder(1)
tower_builder(2)
tower_builder(3)