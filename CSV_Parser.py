import re
import csv
import os

filepath = "G:\\Enterprise Security\\Cybersecurity Team\\Security Incidents\\CCleaner 9-21\\"
#pattern=re.match("ab\w.+\.com")
is_in_file = False

def create_parser(filepath,filename,regularexpression,CSVcolumn):
	filepath= input('Copy file Path here')
	filename=input("Copy CSV file: here")
	regularexpression = input("Place your regular expression here:")
	CSVcolumn= input("what column # are you searching in? : ")
	with open(filepath+filename, 'rb') as csvfile:
		my_content = csv.reader(csvfile, delimiter=',')
		for line in my_content:
			if re.match('"'+regularexpression+'"',line[CSVcolumn]):
				print line
			else:
				print 'nothing found'
			#if username in row:
				#is_in_file = True



create_parser(1,2,3,4)