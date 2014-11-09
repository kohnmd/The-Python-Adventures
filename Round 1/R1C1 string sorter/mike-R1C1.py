# Grab the string.
str_file = open('string.txt', 'r')
orig_str = str_file.read()

# Turn the string into a list.
orig_str_list = orig_str.split(' ')

# Initialize a few empty lists. We'll use these later.
int_list = []
str_list = []
sorted_list = []


# Loop through the orig_str_list pieces.
for piece in orig_str_list:

	# Check if this shit is an int.
	try:
		piece = int(piece)
		# If we've made it this far, the previous line didn't throw an error.
		# Therefore, the piece is an int. Also, this converts the piece from
		# a string to an int.
		int_list.append(piece)
		
	except ValueError:
		# If we're here, int(piece) threw an error, therefore the piece is a string.
		str_list.append(piece)
		
		
# Now sort each individual list. The str_list is using a case-insensitive sort.
int_list = sorted(int_list)
str_list = sorted(str_list, key=lambda s: s.lower())


# Finally, loop through the orig_str_list again to build the sorted one.
# For every int we come across, take the first int out of the sorted int_list
# and add it to the sorted_list. Same with the str_list for every string.
for piece in orig_str_list:

	# Check if that shit is an int.
	try:
		int(piece)
		# Remove the first item from the int_list and add it to the end of the sorted list.
		# Convert it to a string again so that the list can be turned into a string again.
		sorted_list.append( str(int_list.pop(0)) )
		
	except ValueError:
		# Remove the first item from the str_list and add it to the end of the sorted list.
		sorted_list.append( str_list.pop(0) )

		
# Booya bitches.
print ' '.join(sorted_list)