# Create variable to make While loop run until it becomes false
not_done = True

while not_done:
	ip_add = input("\n\nPlease enter an IP address: ")

	# IP address is valid until proven otherwise

	valid_ip = True
	# Split the IP address into octets
	octets = ip_add.split(".")
	# Check that we have four octets or go back to top of While loop
	if len(octets) != 4:
		print("\nSorry but you didn't put in four octets. Please try again.")
		continue

	"""Try to convert the strings in the list "octets" to integers, if not
	   successful raise ValueError and go back to top of loop."""

	for index, octet in enumerate(octets):
		try:
			octets[index] = int(octet)
		except ValueError:
			valid_ip = False

	# Go back to top of loop if IP is not valid
	if not valid_ip:
		print("""\nYou entered an octet that wasn't an integer or a blank -
			that's not going to work""")
		continue

	# Store each slice of "octets" in its own variable

	first_octet, second_octet, third_octet, fourth_octet = octets

	# Check validity of first octet

	if first_octet < 1:
		valid_ip = False
	elif first_octet > 223:
		valid_ip = False
	elif first_octet == 127:
		valid_ip = False

	# Check that IP is not from 169.254.0.0/16 range

	if first_octet == 169 and second_octet == 254:
		valid_ip = False

	# Verify that 2nd, 3rd and 4th octet is not less than 0 or larger than 255

	for octet in (second_octet, third_octet, fourth_octet):
		if (octet < 0) or (octet > 255):
			valid_ip = False

	# If the IP is valid, exit the script and print the IP address

	if valid_ip:
		not_done = False
	else:
		print("\nThe IP address entered was not valid, please try again.")

# Print the IP address
print("\n\nThe IP address is valid: {}".format(ip_add))

