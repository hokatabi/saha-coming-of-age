import json, random, config, content, sentence
from requests_oauthlib import OAuth1Session
from datetime import datetime

def lambda_handler(event, context):

    text = ""
    now = datetime.now()

    if now.hour == 0 and now.minute == 0:
        text = content.count_coming_of_age()
    elif now.weekday() == 4 or now.weekday() == 5 and now.hour == 23 and now.minute == 55:
        text = random_sentence(sentence.寝る5分前)
    elif now.weekday() != 4 and now.weekday() != 5 and now.hour == 21 and now.minute == 55:
        text = random_sentence(sentence.寝る5分前)

    if text == "":
        return 0
    else:
        output(event, text)

def output(event, content):

    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status" : content}

    if event == "local":
        print(content)
    else: 
        res = twitter.post(url, params = params)
        if res.status_code == 200:
            print("Success.")
        else:
            print("Failed. : %d"% res.status_code)

def random_sentence(listname):

    num = len(listname)
    return str(listname[random.randint(0, num-1)])
