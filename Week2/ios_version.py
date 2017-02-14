cisco_ios = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M),
 Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"""

# Split the string into several parts and store in list "cisco_ios_list"

cisco_ios_list = cisco_ios.split(",")

# Store version in "ios_version" and strip "\n" from it

ios_version = cisco_ios_list[2]
ios_version = ios_version.strip()

# Split into two parts, one with "Version " and other version number

ios_version = ios_version.split("Version ")[1]

# Print the IOS version

print(ios_version)
