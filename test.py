# Just writing some basic code to check branching

def sum_of_list(l):
	if l == []:
		return 0
	else:
		return l[0]+sum_of_list(l[1:])

# Tests

sum_of_list(range(10)) # 55

sum_of_list([n*n for n in range(10)]) # unknown
