input_array = [21,4,1,3,9,20,25]


#no_flip = False
count = 0
while count <3:
	#no_flip = True
	count += 1
	for i in range(len(input_array)):
		if i+1 < len(input_array):
			if input_array[i] > input_array[i+1]:
				temp = input_array[i]
				input_array[i] = input_array[i+1]
				input_array[i+1] = temp
				no_flip = False

print input_array

