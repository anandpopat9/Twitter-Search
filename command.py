import os
import time
import json
id_anand1=776717933779103743
for i in range(0,100):
    os.system("curl --get 'https://api.twitter.com/1.1/search/tweets.json' --data 'count=100&lang=ko&max_id="+str(id_anand1)+"&q=%23iphone7+OR+%23Watch2+OR+%23iphone7Plus+OR+%23gameofthrones' --header 'Authorization: OAuth oauth_consumer_key=\"c0VOOxyIhvWEFNL2GZMdxKH1h\", oauth_nonce=\"ee5269ad99caf7a36d0806ebab1d5f88\", oauth_signature=\"riHkO6XiFlu4D6u6%2BIsP7%2FHhBpw%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1474145881\", oauth_token=\"777239895094026240-38W7aaY0fsiNnKjCYQdVGa7ahovMC0R\", oauth_version=\"1.0\"' --verbose >> /Users/anandpopat/downloads/a/ko/main_ko"+str(i)+".json")
    time.sleep(2)

    file = open("/Users/anandpopat/downloads/a/ko/main_ko"+str(i)+".json","r")
    tweet=json.load(file)
    for a in tweet['statuses']:
        id_anand=a['id']
        id_anand1=id_anand-1
    print str(id_anand1)+"------"+str(i)

