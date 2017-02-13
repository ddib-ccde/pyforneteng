"""Use built-in function "input()" to ask for an IP address
   and store it in a variable named ip_add."""

ip_add = input("Enter an IP address: ")

"""Use the built-in function "split()" to split the IP address
   into octets where a dot is the delimiter."""

ip_octet = ip_add.split(".")

# Discard anything beyond the first three strings

ip_octet = ip_octet[:3]

"""Use the built-in function "append()" to add a zero
   at index 3 in the list."""

ip_octet.append("0")

"""Use the built-in function "join()" to join the strings
   back into one string with a dot as a delimiter."""

ip_new = ".".join(ip_octet)

print("Your network is: {}".format(ip_new))

"""Print a table with network number, first octet in binary,
   first octet in hex and make the table left aligned. 
   The string must first be converted into an integer before
   "bin()" or "hex()" can be used."""

first_octet_bin = bin(int(ip_octet[0]))
first_octet_hex = hex(int(ip_octet[0]))

print("\n\n")
print("{:<20} {:<20} {:<20}".format("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX"))
print("{:<20} {:<20} {:<20}".format(ip_new, first_octet_bin, first_octet_hex)) 
