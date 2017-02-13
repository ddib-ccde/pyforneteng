# Ask user for IP address
ip_add = input("\n\nPlease enter an IP address: ")

# Use "split()" to split the IP address into octets

octets = ip_add.split(".")

first_octet_bin = bin(int(octets[0]))
second_octet_bin = bin(int(octets[1)])
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

# Print left aligned tables that are 20 chars wide

print("\n\n")
print("{:<20} {:<20} {:<20} {:<20}".format("first_octet", "second_octet", "third_octet", "fourth_octet"))
print("{:<20} {:<20} {:<20} {:<20}".format(first_octet_bin, second_octet_bin, third_octet_bin, fourth_octet_bin))