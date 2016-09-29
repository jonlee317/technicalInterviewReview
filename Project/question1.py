# 
# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.
# 

def question1(s, t):
	substringLength = len(t)
	stringLength = len(s)
	beginIndex = 0
	endIndex = beginIndex + substringLength
	matchedNum = []
	checkList = [0 for i in range(substringLength)]
	while endIndex <= stringLength:
		testSubstring = list(s[beginIndex:endIndex])
		mySubstring = list(t)
		mySubstringLength = len(mySubstring)
		print (testSubstring)
		print (mySubstring)

		# seach through testsubstring
		while len(testSubstring) >0:
			testChar = testSubstring.pop()
			print ("here is test char")
			print(testChar)
			for i in range(mySubstringLength):
				print (i)
				print (mySubstring)
				if mySubstring[i] == testChar and checkList[i] ==0:
					matchedNum.append(1)
					checkList[i] += 1
					print (matchedNum)

		if matchedNum.count(1) == substringLength:
			break
		else:
			matchedNum = []
			checkList = [0 for i in range(substringLength)]

		beginIndex += 1
		endIndex += 1
		print (matchedNum)

	if matchedNum.count(1) == substringLength:
		return True
	else:
		return False
  
# testcode
print(question1("udacity", "yit"))

