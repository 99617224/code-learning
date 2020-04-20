import twint

c=twint.Config()
c.username='出埃及记'
c.Limit='20'
# c.Store_object='True'
# c.Format = 'ID{id}|用户名{username}'
twint.run.Search(c)
# tweets=twint.output.tweets_list
# for i in tweets:
#     print(type(i))
#     print(i)