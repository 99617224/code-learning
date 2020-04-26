import twint
import time
import datetime
tweets=[]
newspeople=[]
newsword=[]
fiveminutesAgo = (datetime.datetime.now() - datetime.timedelta(minutes=10))
c=twint.Config()
c.Search='#BREAKING'
c.Count='True'
c.Lang='en'
c.Store_object='True'
c.Since=fiveminutesAgo.strftime("%Y-%m-%d %H:%M:%S")
c.Store_object_tweets_list=tweets
c.Limit='1'
# c.Translate='True'
# c.TranslateDest='zh'
twint.run.Search(c)

for i in tweets:
    print(i.tweet)