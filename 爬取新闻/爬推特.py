import twint

c=twint.Config()
c.Search='BREAKING'
c.Limit='20'
c.Store_object='True'
# c.Format = 'ID{id}|用户名{username}'
twint.run.Search(c)
tweets=twint.output.tweets_list
for i in tweets:
    print(i.username+'发送了以下内容'+i.tweet)
    print(type(i))