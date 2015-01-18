import sys

numbers_list = [1,1,2,1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
extra_numbers = [6,7,8,9]

extra_num = 5
print("---")

def look_for_2( index ):
	n = 0
	number_looking_for = numbers_list[index]
	for i in range(len(numbers_list)):
		if i == index:
			continue
		for j in range( i + 1, len(numbers_list)):
			if (j == index):
				continue
			
			if( ( numbers_list[j] + numbers_list[i] ) == number_looking_for ):
				n = n + 1
				# print(str(numbers_list[j]) + " + " + str(numbers_list[i]) )
	return n

def look_for_3( index ):
	n = 0
	number_looking_for = numbers_list[index]
	for i in range(len(numbers_list)):
		if i == index:
			continue
		for j in range( i + 1, len(numbers_list)):
			if (j == index):
				continue
			for k in range(j + 1, len(numbers_list)):
				if (k == index ):
					continue

				if( ( numbers_list[k] + numbers_list[j] + numbers_list[i] ) == number_looking_for ):
					n = n + 1
					# print(str(numbers_list[k]) + " + " + str(numbers_list[j]) + " + " + str(numbers_list[i]) )
	return n

def look_for_4( index ):
	n = 0
	number_looking_for = numbers_list[index]
	for i in range(len(numbers_list)):
		if i == index:
			continue
		for j in range( i + 1, len(numbers_list)):
			if (j == index):
				continue
			for k in range(j + 1, len(numbers_list)):
				if (k == index ):
					continue
				for l in range(k + 1, len(numbers_list)):
					if (l == index ):
						continue

					if( ( numbers_list[l] + numbers_list[k] + numbers_list[j] + numbers_list[i] ) == number_looking_for ):
						n = n + 1
						# print(str( numbers_list[l] ) + " + " + str(numbers_list[k]) + " + " + str(numbers_list[j]) + " + " + str(numbers_list[i]) )
	return n

def look_for( index ):
	n = 0
	number_looking_for = numbers_list[index]
	# print number_looking_for
	n2 = look_for_2( index )
	n3 = look_for_3( index )
	n4 = look_for_4( index )
	# print( n2)
	# print( n3)
	# print( n4)
	n = n2 + n3 + n4
	return n

for i in range(len(numbers_list)):
	number_looking_for = numbers_list[i]
	n = look_for( i )
	print( str(number_looking_for) + " : " + str( n ) )