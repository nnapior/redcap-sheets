# import libraries
import requests, json, os

# global variable for url
url = "https://dri.udel.edu/redcap/api/"

# a function to get the project records from the database
def getRecords(apiKey):
	# set up request
	data = {
		'token': apiKey,
		'content': 'record',
		'format': 'json',
		'type': 'flat'
	}
	
	#make the request
	r = requests.post(url, data=data)
	
	# is the result ok?
	if(r.status_code == 200):
		# create a json object from the result and return it
		jsonObject = json.loads(r.text)
		return jsonObject
	# if not, print the error and return None
	else:
		print("error "+str(r.status_code)+": "+r.text)
		return None

def getAPIKey():
	configFile = open("config.json","r")
	content = json.loads(configFile.read())
	return content["api_key"]

# main function
if __name__ == "__main__":
	# get the api key from config.json
	apiKey = getAPIKey()
	
	# get the raw records object
	jsonObject = getRecords(apiKey)
	
	# for each record...
	i = 1
	for item in jsonObject:
		# save the event name and participant id
		participantID = item["participant_id"]
		eventName = item["redcap_event_name"]
		
		# create a new file based on the event name
		outputFile = open(eventName+".csv", 'w')
		
		# get the keys of the record dictionary
		keys = list(item.keys())
		
		# set up the CSV header and insert the participant id
		headerStr = "participant_id"
		valueStr = participantID
		
		# for each key in the record...
		for key in keys[2:]:
			# add the key to the CSV header
			headerStr+=", "+key
			# add the value to the current row. if no value exists, add "n/a"
			if(item[key] == ''):
				valueStr+=", n/a"	
			else:
				# sanitize input (remove newlines and tabs)
				valueStr+=", "+item[key].replace("\r","").replace("\n"," ").replace("\t"," ")
				
		# write the header to the file
		outputFile.write(headerStr+"\n")
		# write the value to the file
		outputFile.write(valueStr)