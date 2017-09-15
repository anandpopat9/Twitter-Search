import json
file = open("/Users/anandpopat/Downloads/a/ko15.json","r")
tweet=json.load(file)
for b in tweet['statuses']:
    id_anand=b['id']
    print id_anand
