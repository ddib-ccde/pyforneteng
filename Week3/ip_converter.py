# Need to import sys for handling command line arguments

import sys

"""Check that exactly two arguments are supplied, script name
   and the IP address. If less than two arguments are supplied
   then user did not enter an IP address. If more than two
   arguments were supplied the user ented too many IP addresses."""

if len(sys.argv) != 2:
    sys.exit("Usage: ./ip_converter.py <IP_ADDRESS>")

"""Extract the IP address by using "pop()" on "sys.argv".
   IP address will be a string."""
   
ip_address = sys.argv.pop()

"""Convert the IP address into a list consisting of octets
   by splitting the string with "split()" and separating on
   a dot"""

octets = ip_address.split(".")

"""Check that "octets" list consists of four strings meaning
   that the IP address is not too short or too long. If it is
   the script will exit"""

# Create empty list where binary octets will be stored

ip_addr_bin = []

if len(octets) == 4:


    # Loop through all octets in the list "octets"

    for octet in octets:
        bin_octet = bin(int(octet))
        # Remove "0b" from the string by removing the first two chars of string
        bin_octet = bin_octet[2:]

        # Use while to loop until "bin_octet" is 8 chars long
        while True:
            if len(bin_octet) >= 8:
                break
            # Prepend a zero to "bin_octet" i.e. padding
            bin_octet = "0" + bin_octet

        # Add "bin_octet" to the "ip_addr_bin" list
        ip_addr_bin.append(bin_octet)
    
    # Join the octets and insert a dot between them making it dotted binary
    ip_addr_bin = ".".join(ip_addr_bin)
    
    # Print left aligned table with IP address and binary address
    print("\n{:<15} {:<45}".format("IP address", "Binary"))
    print("{:<15} {:<45}".format(ip_address, ip_addr_bin))

else:
    sys.exit("Invalid IP address entered...")