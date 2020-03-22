import json, config
from datetime import datetime


def count_coming_of_age():

    year = config.year
    month = config.month
    day = config.day

    today = datetime.now()
    twenty_coming_day = datetime(year+20, month, day)
    twenty_distance = twenty_coming_day - today
    eighteen_coming_day = datetime(year+18, month, day)
    eighteen_distance = eighteen_coming_day - today

    text = today.strftime('%Y年%m月%d日') + 'になりました。'

    if today.month == month and today.day == day:
        age = today.year - year
        text = text + '今日は' + str(age) + '歳のお誕生日だよ！やったね！🎉'

    elif today.day == day:
        age = today.year - year
        age_month = today.month - month

        if today.month < month:
            age = age - 1
            age_month = 12 + age_month

        text = text + '今日で' + str(age) + '歳' + str(age_month) + 'ヶ月だよ⭐'

    text = text + '🔞クリアまであと' + str(eighteen_distance.days) + '日だよ。'
    text = text + '20まであと' + str(twenty_distance.days) + '日だよ。'

    return(text)
