"""

Given an array what is the most frequently occuring element

"""
def most_frequent(list):
	count = {} # dictionary
	max_count = 0
	max_item = None

	for i in list:
		if i not in count:
			count[i] = 1

		else:
			count[i] += 1

		if count[i] > max_count:
			max_count = count[i]
			max_item = i

	return max_item

print(most_frequent([1,3,3,3,2,1,1,1]))




'''
def frequent_element(box):

	any = [1,2,3,3,4]

	ele = 0

	for ele_count in range(box):

		ele += 1

		if i in box > 1:
			ele_count = ele.count()

			return ele_count
print(max(frequent_element([1,2,3,3,4])))


'''


