import csv
import json

csv_file = 'TempData.csv'

# initiate dataList
dataDict = {}

# open correct infile
with open(csv_file, newline = '') as csvfile:
	rows = csv.reader(csvfile)

	i = 0
	# for every row in file
	for row in rows:

		# if not empty and doesn't start with #
		if not row[0].startswith('#'):

			if int(row[0]) == 10:
				if i == 0:
					dataDict['Sweden'] = {}
					dataDict['Sweden']['Maximum'] = []
					dataDict['Sweden']['Minimum'] = []
					dataDict['Sweden']['Average'] = []
					dataDict['Sweden']['Average'].append({'Date': row[1], 'Temperature': row[2]})
					dataDict['Sweden']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
					dataDict['Sweden']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
					i += 1
				else:
					dataDict['Sweden']['Average'].append({'Date': row[1], 'Temperature': row[2]})
					dataDict['Sweden']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
					dataDict['Sweden']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			elif int(row[0]) == 13:
				if i == 1:
					dataDict['Austria'] = {}
					dataDict['Austria']['Maximum'] = []
					dataDict['Austria']['Minimum'] = []
					dataDict['Austria']['Average'] = []
					dataDict['Austria']['Average'].append({'Date': row[1], 'Temperature': row[2]})
					dataDict['Austria']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
					dataDict['Austria']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
					i += 1
				else:
					dataDict['Austria']['Average'].append({'Date': row[1], 'Temperature': row[2]})
					dataDict['Austria']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
					dataDict['Austria']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 269:
			# 	if i == 2:
			# 		dataDict['Flevoland'] = {}
			# 		dataDict['Flevoland']['Maximum'] = []
			# 		dataDict['Flevoland']['Minimum'] = []
			# 		dataDict['Flevoland']['Average'] = []
			# 		dataDict['Flevoland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Flevoland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Flevoland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Flevoland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Flevoland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Flevoland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 270:
			# 	if i == 3:
			# 		dataDict['Friesland'] = {}
			# 		dataDict['Friesland']['Maximum'] = []
			# 		dataDict['Friesland']['Minimum'] = []
			# 		dataDict['Friesland']['Average'] = []
			# 		dataDict['Friesland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Friesland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Friesland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Friesland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Friesland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Friesland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 275:
			# 	if i == 4:
			# 		dataDict['Gelderland'] = {}
			# 		dataDict['Gelderland']['Maximum'] = []
			# 		dataDict['Gelderland']['Minimum'] = []
			# 		dataDict['Gelderland']['Average'] = []
			# 		dataDict['Gelderland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Gelderland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Gelderland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Gelderland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Gelderland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Gelderland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 277:
			# 	if i == 5:
			# 		dataDict['Groningen'] = {}
			# 		dataDict['Groningen']['Maximum'] = []
			# 		dataDict['Groningen']['Minimum'] = []
			# 		dataDict['Groningen']['Average'] = []
			# 		dataDict['Groningen']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Groningen']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Groningen']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Groningen']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Groningen']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Groningen']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 280:
			# 	if i == 6:
			# 		dataDict['Drenthe'] = {}
			# 		dataDict['Drenthe']['Maximum'] = []
			# 		dataDict['Drenthe']['Minimum'] = []
			# 		dataDict['Drenthe']['Average'] = []
			# 		dataDict['Drenthe']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Drenthe']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Drenthe']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Drenthe']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Drenthe']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Drenthe']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 290:
			# 	if i == 7:
			# 		dataDict['Overijssel'] = {}
			# 		dataDict['Overijssel']['Maximum'] = []
			# 		dataDict['Overijssel']['Minimum'] = []
			# 		dataDict['Overijssel']['Average'] = []
			# 		dataDict['Overijssel']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Overijssel']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Overijssel']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Overijssel']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Overijssel']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Overijssel']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 310:
			# 	if i == 8:
			# 		dataDict['Zeeland'] = {}
			# 		dataDict['Zeeland']['Maximum'] = []
			# 		dataDict['Zeeland']['Minimum'] = []
			# 		dataDict['Zeeland']['Average'] = []
			# 		dataDict['Zeeland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Zeeland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Zeeland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Zeeland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Zeeland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Zeeland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 344:
			# 	if i == 9:
			# 		dataDict['Zuid-Holland'] = {}
			# 		dataDict['Zuid-Holland']['Maximum'] = []
			# 		dataDict['Zuid-Holland']['Minimum'] = []
			# 		dataDict['Zuid-Holland']['Average'] = []
			# 		dataDict['Zuid-Holland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Zuid-Holland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Zuid-Holland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Zuid-Holland']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Zuid-Holland']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Zuid-Holland']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 370:
			# 	if i == 10:
			# 		dataDict['Noord-Brabant'] = {}
			# 		dataDict['Noord-Brabant']['Maximum'] = []
			# 		dataDict['Noord-Brabant']['Minimum'] = []
			# 		dataDict['Noord-Brabant']['Average'] = []
			# 		dataDict['Noord-Brabant']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Noord-Brabant']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Noord-Brabant']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Noord-Brabant']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Noord-Brabant']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Noord-Brabant']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})

			# elif int(row[0]) == 380:
			# 	if i == 11:
			# 		dataDict['Limburg'] = {}
			# 		dataDict['Limburg']['Maximum'] = []
			# 		dataDict['Limburg']['Minimum'] = []
			# 		dataDict['Limburg']['Average'] = []
			# 		dataDict['Limburg']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Limburg']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Limburg']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})
			# 		i += 1
			# 	else:
			# 		dataDict['Limburg']['Average'].append({'Date': row[1], 'Temperature': row[2]})
			# 		dataDict['Limburg']['Minimum'].append({'Date': row[1], 'Temperature': row[3]})
			# 		dataDict['Limburg']['Maximum'].append({'Date': row[1], 'Temperature': row[4]})



# outfile name
json_file = 'TempData.json'

# dump data into the outfile
with open(json_file, 'w') as outfile:
    outfile.write(json.dumps(dataDict))