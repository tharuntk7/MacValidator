#!/usr/bin/env python

__author__ = "Tharun Kumar"
__email__ = "tharunkumartk@gmail.com"
__copyright__ = "Copyright 2020, An Agnostic Project"
__credits__ = ["Tharun Kumar"]
__maintainer__ = "Tharun Kumar"
__license__ = ""
__version__ = "0.0.1"
__status__ = "Development"
__Description__="To check if the entered MAC address whose format is valid or not"



import re

class MacAddress:
	def MacValidate(macaddr):
		if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", macaddr.lower()):
			return True
		elif re.match("[0-9a-f]{4}([.]?)[0-9a-f]{4}([.]?)[0-9a-f]{4}$",macaddr.lower()):
			return True
		else:
			return False