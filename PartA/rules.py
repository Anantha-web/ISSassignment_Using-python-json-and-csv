#json modules to read json files
import json

#function to convert the json file into dictionary
def jsonTO_dic():
	# Opening JSON file and coverting to dictionary
	with open('rules.json') as json_file:
		data = json.load(json_file)
	
	return data
