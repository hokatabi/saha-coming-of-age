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

    today = datetime.datetime.now()
    twenty_coming_day = datetime.datetime(year+20, month, day)
    twenty_distance = twenty_coming_day - today
    eighteen_coming_day = datetime.datetime(year+18, month, day)
    eighteen_distance = eighteen_coming_day - today

    tweet = today.strftime('%Y年%m月%d日') + 'になりました。'

    if today.month == month and today.day == day:
        age = today.year - year
        tweet = tweet + '今日は' + str(age) + '歳のお誕生日だよ！やったね！🎉'

    elif today.day == day:
        age = today.year - year
        age_month = today.month - month

        if today.month < month:
            age = age - 1
            age_month = 12 + age_month

        tweet = tweet + '今日で' + str(age) + '歳' + str(age_month) + 'ヶ月だよ⭐'

    tweet = tweet + '🔞クリアまであと' + str(eighteen_distance.days) + '日だよ。'
    tweet = tweet + '20まであと' + str(twenty_distance.days) + '日だよ。'

    params = {"status" : tweet}

    print(tweet)

    res = twitter.post(url, params = params)

    if res.status_code == 200:
        print("Success.")
    else:
        print("Failed. : %d"% res.status_code)
