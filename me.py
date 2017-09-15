import sys
import re
import codecs
import unicodedata
import ast
import json
from datetime import datetime

file_w = open('/Users/anandpopat/desktop/demonetization/demonetization.json','a')
for i in range(17,45):
	file_r = open('/Users/anandpopat/desktop/demonetization/demonetization'+str(i)+'_pfs.json','r')###change topic
	for line in file_r:
		#print(type(line))
		#file_w.write(line)
		d = json.loads(line)
		file_w.write(json.dumps(d))
		file_w.write("\n")

