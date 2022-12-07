"""
Given a string of words, reverse all the words

start = "This is the best"
finish = "best the is This"

"""

def reverse(s):

	length = len(s)
	spaces = [' ']
	words = []
	i = 0 # Index tracker

	while i < length:
		if s[i] not in spaces: # if index at zero is not in a space 
		    word_start = i

		    while i < length and s[i] not in spaces:
		    	i += 1

		    words.append(s[word_start:i])

		i += 1

	return "".join(reversed(s))



    # s = s.split()
	# return " ".join(reversed(s.split()))
	# return "*".join(s.split()[::-1]) //Alternative way

	'''
	def rev(s):
		return s.split()[::-1]
	print(rev('Hello, I am me'))
	//Useful in ML
    '''
print(reverse("This is the best"))