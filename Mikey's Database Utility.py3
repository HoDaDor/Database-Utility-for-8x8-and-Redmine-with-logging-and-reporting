#!/usr/bin/env python

# Import agent info from config file
import json

# Load the configuration file
with open('UserConfig.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

# Mikey's Database Tool Start




# Create new csv file or append to existing based on setting from config file
# Maybe ask new file or append every login? Or set rollover date.

# Interface with 8x8 and identify incoming caller's phone number
# Use phone number, export to ID function to correlate phone number to customer name and organizaion
# ID function uses a customer database and returns related info as array

# Enumerate session ID and record customer ID to agent shift CSV
