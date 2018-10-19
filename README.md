# Database-Utility-for-8x8 Virtual Call Center and Redmine Ticketing System

***Work in progress***

Interface with 8x8 Virtual Call Center and Redmine Ticketing System with automatic logging/reporting


Flow:
- Service Rep logs in
- New log emtry created (Log to single file with new cycle beginning on the 1st of each month.) 
- Date, time, and agent info recorded in log
- Standby mode with keepalive to prevent system sleep and listen for incoming 8x8 data

Call from 8x8:
- Extract incoming phone number and checks local (or cloud) customer database for customer info to display to agent
- Enumerate and log customer info to session upon agent confirmation/acceptance of call. 
- If no agent response, create or append session to secondary log.
- 


User initiated by Calling 8x8 system
- 8x8 connects to service rep
- Extract phone number from 8x8 call center solutions API 
- Cross-reference with local database CSV to associate phone to Email and Customer ID (Either Excel or Google Sheets)
- Automatically input info to current CSV file and enumerate (Create new CSV if new session)

Input requirements:
- from phone number only using 8x8 API
- User Info

Output Requirements:
- To database (CSV or Excel but ideally an online cloud form such as Google Sheets)

Database to use the following fields:
Session #
Date
Call Start Time
Call End Time
Customer First Name
Customer Last Name
Organization Requesting Support
Block Verification (Verification through Manual Entry or Extract from local database)
RM # (Extract from 8x8 API)
8x8 Case ID# (Extract from 8x8 API)



Addon Extras:

Web Ui:
- User Info
- from web
- from excel



RedMine Ticketing System (For agent use to submit tickets for dev team):
							#Field data from redmine ticket dahboard
All subject 
Status
Date due
Last modified date
Transaction Code
Action




Additional Projects:
Online training seminar (video series) 
