#!/usr/bin/python3

# Import agent info from config file
import yaml
import requests
import xlwt
import conjunction_junction
from member_lookup import caller_lookup
from gettime_ntp import current_time

# Database Logging Util Start
def main():

    # Use 8x8 Virtual Contact Center Real Time Statistics Reporting API
    # to get incoming caller phone number

    # Check for internet connection
    try:
        socket.create_connection(('1.1.1.1', 80))
    # If no internet connection, ask for user prefernce.
    # This could also be set in config file so user won't
    # be asked every time.
    except socket.error as msg:
        print "Not connected to the internet."
        darling_picky = input("Wait for connection or continue anyway? [Y]es or [N]o ")

    # If yes, wait for internet connection
    if darling_picky == "Y":
        pass# Incomplete, don't forget this guy here!

    # If no, continue and use time from system clock
    if darling_picky == "N":
        current_date = date.today().strftime('%m/%d/%Y')

    # Check current date. If date matches or less than last date, start new log
    # Else, append current session to current log
    if current_date == date.today().strftime('%m/%d/%Y'):
        pass

    # Enumerate session ID and record customer ID to agent shift CSV
    session_id_update = lastsession_id.conjunction_junction()# Fix?

    # Sleep and wait for call

    # Retrieve member info from caller phone number
    caller_info = caller_lookup.member_lookup(caller_phone)

    # Write caller info to current session log
    set_lastsession.session_id_update

    # End current session with end time and write to log


if __name__ == '__main__':
    main()
