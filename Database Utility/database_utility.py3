#!/usr/bin/env python

# Import agent info from config file
import yaml
import requests
import xlwt
import member_lookup as caller_lookup

# Database Logging Util Start
def main():

	# Use 8x8 Virtual Contact Center Real Time Statistics Reporting API to get incoming caller phone number

	# Check current date. If date matches or less than last date, start new log
	# Else, append current session to current log

	# Enumerate session ID and record customer ID to agent shift CSV

	#Retrieve member info from caller phone number
	caller_info = caller_lookup.member_lookup(caller_phone)

	#Write caller info to current session log

	#End current session with end time and write to log

if __name__ == '__main__':
	main()