# Import pretty print
import pprint

# Define constants used to convert years, weeks, days to seconds
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

# Define variables containing hostnames and uptime
uptime1 = "wb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes"
uptime2 = "3750RJ uptime is 1 hour, 29 minutes"
uptime3 = "CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes"
uptime4 = "rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes"

# Create two empty dictionaries for storing hostname and uptime
uptime_dict = {}
uptime_dict2 = {}

# Use For loop to loop through the uptime values
for uptime in (uptime1, uptime2, uptime3, uptime4):

	# Split uptime with comma as delimiter to get managable chunks
	uptime_fields = uptime.split(",")

	"""Extract hostname from variable "uptime_fields" by using split().
       Delimiter is " uptime is " so whatever comes before " uptime is "
       is the hostname and what comes after is part of the uptime. 
       By using " uptime is " as the delimiter we remove this text
       from our list."""

	(hostname, time_field1) = uptime_fields[0].split(" uptime is ")
	uptime_fields[0] = time_field1

	# Initialize uptime_seconds as 0
	uptime_seconds = 0
	# Loop through each string in the list "uptime_fields"
	for time_field in uptime_fields:

		# Check if there are any years in the uptime
		if "year" in time_field:
			(years, junk) = time_field.split(" year")
			try:
				uptime_seconds += int(years) * YEAR_SECONDS
			except ValueError:
				print("Error during string conversion to integer")

		elif "week" in time_field:
			(weeks, junk) = time_field.split(" week")
			try:
				uptime_seconds += int(weeks) * WEEK_SECONDS
			except ValueError:
				print("Error during string conversion to integer")

		elif "day" in time_field:
			(days, junk) = time_field.split(" day")
			try:
				uptime_seconds += int(days) * DAY_SECONDS
			except ValueError:
				print("Error during string conversion to integer")

		elif "hour" in time_field:
			(hours, junk) = time_field.split(" hour")
			try:
				uptime_seconds += int(hours) * HOUR_SECONDS
			except ValueError:
				print("Error during string conversion to integer")

		elif "minute" in time_field:
			(minutes, junk) = time_field.split(" minute")
			try:
				uptime_seconds += int(minutes) * MINUTE_SECONDS
			except ValueError:
				print("Error during string conversion to integer")

	# Insert number of seconds in dictionary under hostname
	uptime_dict[hostname] = uptime_seconds
