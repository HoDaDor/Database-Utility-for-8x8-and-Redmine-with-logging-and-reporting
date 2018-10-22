#!/usr/bin/env python
import yaml

def getToDaConfig():
	
	# Load config info
	with open(UserConfig.yaml, "r") as configurization:
		data=yaml.load(configurization)
	# Output meow!
	return configurization
