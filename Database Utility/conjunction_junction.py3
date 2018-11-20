#!/usr/bin/python3

# Importable functions library

import xlsxwriter
import csv
from openpyxl import workbook

# Logger function logs to Excel document
def lumberjack():

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.workbook('mikey_logsheet.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row & column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)

    # Insert an image.
    worksheet.insert_image('B5', 'logo.png')

    workbook.close()

# Function to get internet time
def gettime_ntp(addr='time.nist.gov'):
    # http://code.activestate.com/recipes/117211-simple-very-sntp-client/
    from socket import *
    import struct
    import sys
    import time
    TIME1970 = 2208988800L
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        return time.ctime(t),t

# Loads members database csv file
# Input is path to members.csv file
# Returns converted list of dictionaries
def member_loader(members):
    with open(members, newline='') as csvfile:
        memberdb = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
    return memberdb
# Search members list and correlates phone number to member name
# Returns all info associated to input phone number
def caller_lookup(caller_phone,memberdb):
    for caller in member_loader():
        if caller['caller_phone'] == caller_phone:
            return caller
