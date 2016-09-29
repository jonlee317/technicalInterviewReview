# Question 2
# Given a string a, find the longest palindromic substring contained in a. 
# Your function definition should look like question2(a), and return a string.


def findMatch(begin, end, output):
	if begin == end:
		output = begin+output+end

	return output


def question2(a):
	outputString = ""
	initialIndex = 0
	finalIndex = initialIndex + 1

	while finalIndex < len(a):
    # Only designed to find any double letters
    # TODO:  need to find double letters and loop or recurse through the neighbors
    # TODO:  need to find a single letter with double letter friends next to it
		if a[initialIndex] == a[finalIndex]:
			outputString = a[initialIndex]+outputString+a[finalIndex]
			print(outputString)
			break
		initialIndex += 1
		finalIndex += 1

question2('supperzz')
  
# test code

question2("bloblobbor")
question2("racecar")
