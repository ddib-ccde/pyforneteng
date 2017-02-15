# Import pprint for prettier printing
import pprint

show_ip_int_brief = """
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0        unassigned      YES     unset       up          up
FastEthernet1        unassigned      YES     unset       up          up
FastEthernet2        unassigned      YES     unset       down        down
FastEthernet3        unassigned      YES     unset       up          up
FastEthernet4        6.9.4.10        YES     NVRAM       up          up
NVI0                 6.9.4.10        YES     unset       up          up
Tunnel1              16.25.253.2     YES     NVRAM       up          down
Tunnel2              16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES     NVRAM       down        down
Vlan10               10.220.88.1     YES     NVRAM       up          up
Vlan20               192.168.0.1     YES     NVRAM       down        down
Vlan100              10.220.84.1     YES     NVRAM       up          up
"""

# Split giant string into a list consisting of each line

show_ip_lines = show_ip_int_brief.split("\n")

# Create empty list for appending extracted information to

show_ip_list = []

# Loop through "show_ip_lines" list

for line in show_ip_lines:
	if "Interface" in line:
		continue

	# Split each line into a list of strings consisting of ifname etc.

	line_split = line.split()

	# Only include lines that are of the correct length(6)

	if len(line_split) == 6:
		# Store info in variables, two of the variables will be discarded
		ifname, ip_add, discard1, discard2, line_status, line_proto = line_split

		# Only keep information if line status and protocol is "up"
		if (line_status == "up") and (line_proto == "up"):
			# Append information to the list "show_ip_list"
			show_ip_list.append((ifname, ip_add, line_status, line_proto))

# Print the information with pretty print

print("\n")
pprint.pprint(show_ip_list)
print("\n")



