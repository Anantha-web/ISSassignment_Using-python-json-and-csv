

#csv module to read write csv files
import csv
import rules

#getting rules into dictionary using rules.py file
data=rules.jsonTO_dic()
  

fields = []
rows = []
  
# reading csv file
with open("data.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for row in rows:
    # checking and comparing each column of a row with rules.json
    flag=0
    for i in data:
    	if i['status']=="In Active":
    		flag=0
    		break
    	elif i['fields']['profession']==row[1] and i['fields']['travel']==row[2] and i['fields']['symptomatic']==row[3] and i['fields']['chronic']==row[4] and i['status']==row[5]:
    		
    		#appending the results data to row
    		row[-1]=(i['results'])
    		flag=1
    		#breaking the loop after getting result
    		break
    # If no combination is found in rules.json then setting result as no Access
    if flag==0:
    	row[-1]=("No Access")
    		

#writing into results.csv
with open('results.csv', mode='w') as data_file:
	#FieldNames
	fieldnames = ['Email', 'Profession', 'Travel','Symptomatic','Chronic','Results']
	
	#Creating csv writer object
	results_writer = csv.writer(data_file)
	
	#writing field names into first row
	results_writer.writerow(fieldnames)
	
	#writing data into rows one by one
	for row in rows:
		results_writer.writerow(row)
    		
    		

