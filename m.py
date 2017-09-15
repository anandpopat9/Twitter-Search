import sys
import json

file=open("/Users/anandpopat/Desktop/tennis/tennis15.json","r")
for line in file:
    line=json.loads(line)
    print line['statuses'][99]['id']
