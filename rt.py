import json

for i in range(45,46):
	file = open("/Users/anandpopat/desktop/demonetization_tweets/new/demonetization"+str(i)+".json","r")
	file2 = open("/Users/anandpopat/desktop/demonetization/demonetization"+str(i)+"_rt.json","a")
	file1=json.load(file)
	for rt in file1['anand']:
		for rt1 in rt['statuses']:
			if(not(rt1['text'].lower().startswith("rt"))):
				file2.write(json.dumps(rt1))
				file2.write("\n")
