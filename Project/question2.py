# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

# TODO: clean up the code and comment what each code does
# TODO: see if there is any other more efficient method to implement

def findMatch(inputString, begin, end, output):
	# to take into account the letter corresponding to 'a' in the dcbabcd pattern
	if end-begin == 2:
		output += inputString[begin+1]
	if begin >=0 and end < len(inputString):
		if inputString[begin] == inputString[end]:
			output = inputString[begin]+output+inputString[end]
			output = findMatch(inputString, begin-1, end+1, output)
		else:
			output = output
	return output

def question2(a):
	outputStringList = []
	outputString_type1 = ""
	outputString_type2 = ""
	initialIndex = 0
	finalIndex = initialIndex + 1

	while finalIndex < len(a):
		# Implements the dcbaabcd pattern
		outputString_type1 = findMatch(a, initialIndex, finalIndex, outputString_type1)
		# Implements the dcbabcd pattern
		outputString_type2 = findMatch(a, initialIndex, finalIndex+1, outputString_type2)

		initialIndex += 1
		finalIndex += 1

		# if there is nothing in the list simply append
		if len(outputStringList) == 0:
			outputStringList.append(outputString_type1)
			outputStringList.append(outputString_type2)
		# If there is something in the list place longer string in front else append
		elif len(outputStringList) > 0:
			if len(outputStringList[0]) > len(outputString_type1):
				outputStringList.append(outputString_type1)
			else:
				outputStringList.insert(0,outputString_type1)
			if len(outputStringList[0]) > len(outputString_type2):
				outputStringList.append(outputString_type2)
			else:
				outputStringList.insert(0,outputString_type2)

		outputString_type1 = ""
		outputString_type2 = ""

	if len(outputStringList) > 0:
		# Since palindrome will never be one character
		if len(outputStringList[0]) > 1:
			return outputStringList[0]
		else:
			return ""
	else:
		return ""

# Test Cases
print("---- Test Cases for question 2 ----")
print(question2('zeabxbaezcc'))
# zeabxbaez
print(question2("bloblobbor"))
# obbo
print(question2("racecar"))
# racecar
print(question2("bloblobbbor"))
# obbbo
print(question2("feffzracecarefz"))
# racecar
print(question2(""))
# ""
print(question2("feffzrasdfdasflijdasfldfjshagwoghioiwehofhasdfljacecarefz"))
# aceaca
print(question2("abcdefghijk"))
# ""    <-- nothing since there is no palinrome
print(question2("abcdeffghijk"))
# ff
