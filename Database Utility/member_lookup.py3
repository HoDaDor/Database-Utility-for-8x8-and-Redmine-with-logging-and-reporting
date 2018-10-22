#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

#Loads members database csv file
#Input is path to members.csv file
#Returns converted list of dictionaries
def member_loader(members):
	with open(members, newline='') as csvfile:
		memberdb = list(csv.reader(csvfile, delimiter=',', quotechar= '"'))
	return memberdb

#Search members list and correlates phone number to member name
#Returns all info associated to input phone number
def caller_lookup(caller_phone,memberdb):
	for caller in member_loader():
		if caller['caller_phone'] == caller_phone:
			return caller