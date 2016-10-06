#
# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.
#

def question1(s, t):
	# defining the lengths of the substring and strings
	substringLength = len(t)
	stringLength = len(s)
	# Defining the start and end index substring length relative to the string
	beginIndex = 0
	endIndex = beginIndex + substringLength
	# Create a clean tally to count matches
	matchedNum = []
	# Create a checklist for each index of the substring characters
	checkList = [0 for i in range(substringLength)]

	# Until the last character of the string is reached we check each partition the string
	# to see if all the characters match with the substring
	while endIndex <= stringLength:
		# the segment of the string which will be compared with the input substring
		testSubstring = list(s[beginIndex:endIndex])
		# converting the substring into a list of characters to use python list methods
		mySubstring = list(t)
		mySubstringLength = len(mySubstring)

		# Search through each character of the testsubstring
		while len(testSubstring) >0:
			testChar = testSubstring.pop()
			for i in range(mySubstringLength):
				if mySubstring[i] == testChar and checkList[i] ==0:
					matchedNum.append(1)
					checkList[i] += 1
		if matchedNum.count(1) == substringLength:
			break # If we found all the characters can exit
		else:
			matchedNum = []
			checkList = [0 for i in range(substringLength)]
		# Increment the begin and end index to check the next partition of the string
		beginIndex += 1
		endIndex += 1

	if matchedNum.count(1) == substringLength:
		return True
	else:
		return False
  
# testcode
print(question1("udacity", "yit"))
