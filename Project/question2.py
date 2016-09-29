# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.
outputStringList = []

def findMatch(inputString, begin, end, output):
	if begin >=0 and end < len(inputString):
		if inputString[begin] == inputString[end]:
			output = inputString[begin]+output+inputString[end]
			output = findMatch(inputString, begin-1, end+1, output)
		else:
			output = output

	return output


def question2(a):
	outputString = ""
	initialIndex = 0
	finalIndex = initialIndex + 1

	while finalIndex < len(a):
    # Only designed to find any double letters
    # TODO:  need to find double letters and loop or recurse through the neighbors
    # TODO:  need to find a single letter with double letter friends next to it
		outputString = findMatch(a, initialIndex, finalIndex, outputString)
		"""
		if a[initialIndex] == a[finalIndex]:
			outputString = a[initialIndex]+outputString+a[finalIndex]
			print(outputString)
			break
		"""
		initialIndex += 1
		finalIndex += 1
		outputStringList.append(outputString)
		outputString = ""
	return outputString

(question2('zeabbaezcc'))
print outputStringList

# test code


question2("bloblobbor")
question2("racecar")
