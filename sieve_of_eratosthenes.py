import math

prime_set = set()
composite_set = set()
x = 2

limit = int(input('Select your max number:  '))

while x < limit:

	if x in composite_set:
		pass

	else:
		prime_set.add(x)
		test_num = x
		#find the multiples of x and add them to the composite set
		while test_num <= limit:
			test_num += x
			composite_set.add(test_num)
	#incrememt x by 1 to continue the loop
	x += 1

prime_set = list(prime_set)
prime_set.sort()
prime_set = set(prime_set)

for num in prime_set: 
	print(num)