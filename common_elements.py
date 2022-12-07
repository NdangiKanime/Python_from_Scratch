"""

Common Elements in Two Sorted Arrays
return the elements 9as an array) between two sorrted arrays of integers (ascending order)
Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9]

"""

def common_elements(a,b):
	p1 = 0
	p2 = 0

	result = []

	while p1 < len(a) and p2 < len(b):
		if  a[p1] == b[p2]:
			result.append(a[p1])
			p1 += 1
			p2 += 2

		elif a[p1] > b[p2]:
			p2 += 1

		else:
			p1 += 1 

	return result

print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))

'''
def common_elements():

	given = [1,2,3,4,5]

	other = [8,7,6,5,4]

	for i in given and other:
		print(i)
	return i

print(common_elements())
'''	