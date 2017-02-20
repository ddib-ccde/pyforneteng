import sys

# Exit script if too few or too many arguments are used

if len(sys.argv) != 2:
	sys.exit("Usage: ./ip_checker.py <IP-ADDRESS>")

# Pop the last string in "sys.argv" to get IP in dotted decimal format

ip_add = sys.argv.pop()

# The IP is good until it's been proven bad, stored in "valid_ip"

valid_ip = True

"""Split the "ip_add" string into "octets" variably by using "split()
   using a dot as the delimiter."""

octets = ip_add.split(".")

# Exit script if number of octets is not four

if len(octets) != 4:
	sys.exit("The number of octets is invalid.")

"""Loop through the list "octets" and convert the strings to integers.
   Use "enumerate()" to get an index which is used for accessing slices
   in the list "octets" and then running "int()" on that slice."""

for index, octet in enumerate(octets):
	"""Use try/except to do the conversion. If it's not possible to
	   convert the octet the script will exit."""
	try:
		octets[index] = int(octet)
	except ValueError:
		sys.exit("\n\nInvalid IP address: {}\n".format(ip_add))

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

# Print if the IP is valid or not

if valid_ip:
	print("\n\nThe IP address is valid: {}".format(ip_add))
else:
	sys.exit("\n\nInvalid IP address: {}".format(ip_add))

	



