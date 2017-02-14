entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

# Create list "entries" consisting of the other lists

entries = [entry1, entry2, entry3, entry4]

# Print the table, left aligned

print("\n{:<20} {:<50}".format("ip_prefix", "as_path"))
 
"""Loop through each list in "entries" and use "split()" to
   find the IP prefix and AS path and then print this info."""
   
for entry in entries:
    entry_split = entry.split()
    ip_prefix = entry_split[1]
    as_path = entry_split[4:-1]
    str_as_path = str(as_path)
    print("{:<20} {:<50}".format(ip_prefix, str_as_path))