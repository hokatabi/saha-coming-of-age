import json, config, datetime
from requests_oauthlib import OAuth1Session


def lambda_handler(event, context):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = "https://api.twitter.com/1.1/statuses/update.json"

    year = config.year
    month = config.month
    day = config.day

    adult_coming_day = datetime.datetime(year+20, month, day)
    today = datetime.datetime.now()
    distance = adult_coming_day - today

    tweet = today.strftime('%Y年%m月%d日') + 'になりました。'

    if today.month == month and today.day == day:
        age = today.year - year
        tweet = tweet + '今日は' + str(age) + '歳のお誕生日だよ！やったね！🎉'

    elif today.day == day:
        age = today.year - year
        age_month = today.month - month

        if today.month < month:
            age_month = 12 + age_month

        tweet = tweet + '今日で' + str(age) + '歳' + str(age_month) + 'ヶ月だよ⭐'

    tweet = tweet + 'smhが成人するまであと' + str(distance.days) + '日です。'

    params = {"status" : tweet}

    print(tweet)

    res = twitter.post(url, params = params)

    if res.status_code == 200:
        print("Success.")
    else:
        print("Failed. : %d"% res.status_code)
