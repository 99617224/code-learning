import twint
import time
tweets=[]
c=twint.Config()
c.Search='BREAKING NEWS'
c.Count='True'
c.Store_object='True'
c.Since='2020-04-19 20:20:20'
c.Store_object_tweets_list=tweets
c.Limit='100'
# c.Translate='True'
# c.TranslateDest='zh'
twint.run.Search(c)
print('分割线————————————————————————————————')
print('id是:'+str(tweets[0].id))
print('conversation_id是:'+tweets[0].conversation_id)
print('datestamp是:'+tweets[0].datestamp)
print('datestamp是:'+tweets[0].timestamp)
print('user_id是:'+str(tweets[0].user_id))
print('username是:'+tweets[0].username)
print('name是:'+tweets[0].name)
print('tweet是:'+tweets[0].tweet)
print('mentions是:'+str(tweets[0].mentions))
print('urls是:'+str(tweets[0].urls))
print('photos是:'+str(tweets[0].photos))
print('replies_count是:'+tweets[0].replies_count)
print('retweets_count是:'+tweets[0].retweets_count)
print('likes_count是:'+tweets[0].likes_count)
print('hashtags是:'+str(tweets[0].hashtags))
print('cashtags是:'+str(tweets[0].cashtags))
print('link是:'+tweets[0].link)
print('user_rt_id是:'+str(tweets[0].user_rt_id))
print('near是:'+tweets[0].near)
print('geo是:'+tweets[0].geo)
print('source是:'+tweets[0].source)
print('retweet_date是:'+tweets[0].retweet_date)

