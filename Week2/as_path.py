entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

# Split the string into parts, separator is space

entry_split = entry1.split()

# Extract network through list slicing and accessing index 1

ip_prefix = entry_split[1]

"""Create a list storing the AS path. The AS path starts at index 4
   and stops at the second last string in the list "entry_split"
   The second last entry is found by using the index -1"""

as_path = entry_split[4:-1]

"""Print table that is 20 chars wide for network and 50 chars
   wide for the AS path. Table is left aligned."""

print("{:<20} {:<50}".format("ip_prefix", "as_path"))

# Print the first entry, convert as_path to string or ".format" breaks

print("{:<20} {:<50}".format(ip_prefix, str(as_path)))

# Print the rest of the entries, a lot of code is duplicated

entry_split = entry2.split()
ip_prefix = entry_split[1]
as_path = entry_split[4:-1]
print("{:<20} {:<50}".format(ip_prefix, str(as_path)))
entry_split = entry3.split()
ip_prefix = entry_split[1]
as_path = entry_split[4:-1]
print("{:<20} {:<50}".format(ip_prefix, str(as_path)))
entry_split = entry4.split()
ip_prefix = entry_split[1]
as_path = entry_split[4:-1]
print("{:<20} {:<50}".format(ip_prefix, str(as_path)))