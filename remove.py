import sys
import re
import codecs
import unicodedata
import ast
import json
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


file_w = open('/Users/anandpopat/desktop/demonetization/demonetization_final3.json','a')###change topic
file_r = open('/Users/anandpopat/desktop/demonetization/demonetization45_pfs.json','r')###change topic 


for line in file_r:
	#print(type(line))
	#file_w.write(line)
	d = json.loads(line)
	d["tweet_text"]=d["tweet_text"].replace('\n','')
	d["tweet_text"]=d["tweet_text"].replace('"','')
	file_w.write('{"id": '+str(d["id"])+', "text": "'+d["tweet_text"]+'"}'+'\n')
		