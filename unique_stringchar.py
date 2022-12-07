"""

Given a string, are all characters unique?
should give a True or False return

May use python built in structures

"""

def unique(string):
	string = string.replace(' ', '')
	return len(set(string)) == len(string) # using python built in function set (an unordered list of item counts elements seperately)


print(unique('a bb cdef'))


def unique_element(s):
	s = s.replace(' ','')
	characters = set()

	for letter in s:
		if  letter in characters:
			return False
		else:
			characters.add(letter)
	return True


print(unique_element('i lkj rew'))
		    

