import sys
import re
import codecs
import unicodedata
import ast
import json
from datetime import datetime


for i in range(45,46):
	file_w = open('/Users/anandpopat/desktop/demonetization/demonetization'+str(i)+'_pft.json','a')###change topic
	file_r = open('/Users/anandpopat/desktop/demonetization/demonetization'+str(i)+'_rt.json','r')###change topic 


	for line in file_r:
		#print(type(line))
		#file_w.write(line)
		print "aaaa"
		d = json.loads(line)
		text = d["text"]
		da = datetime.strptime(d['created_at'],'%a %b %d %H:%M:%S +0000 %Y')# format for solr YYYY-MM-DDThh:mm:ssZ
		#print(d.strftime('%Y%m%d'))
		print "aaa"
		d["tweet_date"] = da.strftime('%Y-%m-%dT%H:%M:%SZ')
		emoti_pat = re.compile(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)')
		emo_pat = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u26FF\u2700-\u27BF])+', re.UNICODE)
		emo_list = re.findall(emo_pat, text)
		emoti_list = re.findall(emoti_pat, text)
		emo_str = ""
		for c in emo_list:
			emo_str = emo_str + c
			
		for c1 in emoti_list:
			emo_str = emo_str + c1
				
		d["tweet_emoticons"] = emo_str
		text = emoti_pat.sub(u'', text)
		text = emo_pat.sub(u'', text)
		text =  re.sub(r'http\S+', '', text)
		text =  re.sub(r'@\S+', '', text)
		text =  re.sub(r'#\S+', '', text)
		d["anand_text"] = text
		print "bbbb"
		file_w.write(json.dumps(d))
		file_w.write("\n")
	

