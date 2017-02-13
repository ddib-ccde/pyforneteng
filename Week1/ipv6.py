ipv6_add = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

"""Use the built-in function split() to divide the IPv6 address
   into eight parts where the colon is used to identify where
   the split should happen."""

ipv6_split = ipv6_add.split(":")

print("IPv6 address split:")
print(ipv6_split)

"""Use the built-in function join() to join the eight parts of
   the IPv6 address into one full IPv6 address again. A colon
   will be inserted between each part to get the address to retain
   its original form"""

ipv6_new = ":".join(ipv6_split)

print("IPv6 address rejoined:")
print(ipv6_new)