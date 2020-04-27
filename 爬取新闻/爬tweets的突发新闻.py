
import twint
import time
import datetime
import telegram

bot = telegram.Bot(token='957820157:AAG2vjz1gyhrxHc07fF_orRwegX_0I1XOvc')
tweets = []
newspeople = []
newsword = ['china','virus']
alreadylist = []
fiveminutesAgo = (datetime.datetime.now() - datetime.timedelta(minutes=5))
c = twint.Config()
c.Search = ['#BREAKING']
c.Count = 'True'
c.Lang = 'en'
c.Store_object = 'True'
c.Since = fiveminutesAgo.strftime("%Y-%m-%d %H:%M:%S")
c.Store_object_tweets_list = tweets
c.Limit = '1'
# c.Translate='True'
# c.TranslateDest='zh'
while True:
    twint.run.Search(c)

    for i in tweets:
        for w in newsword:
            if w in i.tweet and i.tweet not in alreadylist:
                print('{0}在{1}{2}发送:{3}.地点：{4}'.format(i.username, str(i.datestamp), 
                str(i.timestamp), i.tweet, i.place))
                bot.send_message(chat_id='-488903601', text='{0}在{1}({2})发送:{3}.地点：{4}'.format(
                i.username, str(i.datestamp), str(i.timestamp), i.tweet, i.place))
                alreadylist.append(i.tweet)
                time.sleep(5)
            else:
                pass
    # print(alreadylist)
    time.sleep(30)