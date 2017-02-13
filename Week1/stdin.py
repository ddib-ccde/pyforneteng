import fileinput

""" Use the function fileinput() to send data through stdin
    to Python. Fileinput() can also read from files but defaults
    to reading from stdin if no arguments are given"""

for line in fileinput.input():
        # Create list consisting of four parts of IP address, separated by "."
        line_split = line.split(".")
        # Remove "\n" from last string in list by using function "rstrip"
        line_split[3] = line_split[3].rstrip()
        print(line_split)
