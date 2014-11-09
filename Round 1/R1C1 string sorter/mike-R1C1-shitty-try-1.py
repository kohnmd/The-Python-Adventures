# Define the string.
mystring = "this 1 is 5 my 4 string right here 7 that is 2 pretty long"

# Turn the string into a list.
mystring_list = mystring.split(" ")

# Initialize a few empty lists. We'll use these later.
int_list = []
str_list = []
int_indeces = []
str_indeces = []

# Loop through list pieces.
for i,piece in enumerate(mystring_list):

	# Check if that shit is an int.
	try:
		int(piece)
		# If we've made it this far, the previous line didn't throw an error.
		# Therefore, it's an int.
		int_list.insert(i, piece)
		int_indeces.append(i)
	except ValueError:
		# If we're here, the int(piece) line threw an error, therefore the
		# piece is an string.
		str_list.insert(i, piece)
		str_indeces.append(i)
		
# Now sort each list and put them together.
int_list_sorted = sorted(int_list)
str_list = sorted(str_list)




"""
MIKE!!!! vvv This shit sucks vvv


sorted_list = []
for i in int_indeces:
	sorted_list.insert((i, int_list))

for i in str_indeces:
	sorted_list[i] = str_list[i]

print( " ".join(sorted_list) )
"""