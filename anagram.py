# Dangi 28/11/22
# Program that takes two words and compares if all letters are the and returns True if they are and False if they're not
def anagram2(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()

	# check if the same number of letters
	if len(s1) != len(s2):
		return False

	# count freequency of each letter
	count = {}

	for letter in s1: # for every letter in first string letter 'c'
	    if letter in count: # if letter is already in my dictionary, then
	        count[letter] += 1 # add 1 to that letter key

	    else:
	    	count[letter] = 1

	    	# do reverse for second string

	for letter in s2:
		if letter in count:
			count[letter] -= 1

		else:
			count[letter] = 1

	for k in count:
		if count[k] != 0:
			return False

	return True
	        

x = anagram2('clint eastwood', 'old West action')

print(x)
