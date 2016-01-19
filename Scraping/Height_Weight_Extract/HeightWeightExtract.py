import json

arrayedIds = open('ids.txt', 'r')
known_hu_ids = arrayedIds.read().split(',')
survey = open('survey.csv', 'rU')
finalfile = open('hw_data.txt', 'w')
allDict= []
dic = {}
count = 0
survey_values = []

for line in survey:
	try:
		survey_values = line.split(',')
	except UnicodeEncodeError:
		pass

	if survey_values[0] in known_hu_ids:
		dic['Sample'] = survey_values[0]
		dic['Height'] = survey_values[4]
		dic['Weight'] = survey_values[5]
		allDict.append(dic)
		dic = {}
		survey_values = []
		count += 1
finalfile.write(str(json.dumps(allDict)))
arrayedIds.close()
survey.close()
finalfile.close()

print allDict
print count





