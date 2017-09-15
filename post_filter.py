import sys
import re
import codecs
import unicodedata
import ast
import json
from datetime import datetime


file_w = open('/Users/anandpopat/Downloads/a/apple_es_lang.json','a')
file_r = open('/Users/anandpopat/Downloads/a/apple_es.json','r')


for line in file_r:
	#print(type(line))
	#file_w.write(line)
	d = json.loads(line)	
	for tweet in d["statuses"]:
		if(not(tweet['text'].lower().startswith("rt"))):
			print("inside if")
			d=datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')# format for solr YYYY-MM-DDThh:mm:ssZ
			#print(d.strftime('%Y%m%d'))
			tweet["tweet_date"] = d.strftime('%Y-%m-%dT%H:%M:%SZ')
			emoti_pat = re.compile(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)')
			emo_pat = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u26FF\u2700-\u27BF])+', re.UNICODE)
			#myre = re.compile(u'['u'\U0001F300-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u26FF\u2700-\u27BF]+', re.UNICODE)
			#myre = re.compile(u'['u'\U0001F300-\U0001F5FF'u'\U0001F600-\U0001F64F'u'\U0001F680-\U0001F6FF'u'\u2600-\u26FF\u2700-\u27BF]+', re.UNICODE)
			temp_dic1 = {"a":tweet["text"]}
			emo_list = re.findall(emo_pat, temp_dic1["a"])
			emoti_list = re.findall(emoti_pat, temp_dic1["a"])
			#tweet["text"] = myre.sub(u'', tweet["text"])
			emo_str = ""
			for c in emo_list:
				dict = {"a":c}
				emo_str = emo_str + c
			
			for c1 in emoti_list:
				dict1 = {"a":c1}
				emo_str = emo_str + c1
				
			tweet["tweet_emoticons"] = emo_str
			tweet["topic"] = "tech"
			file_w.write(json.dumps(tweet))
			file_w.write("\n")

