def get_primelist(upper):
	result = []
	for cp in range ( 2, upper + 1 ):
		for i in range ( 2, cp ):
			if ( cp % i == 0 ):
				break
		else:
			result.append(cp)
	return result

# RUN to create an array of the prime numbers
# [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#  43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
print (get_primelist(100000))