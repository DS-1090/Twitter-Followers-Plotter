import tweepy
import matplotlib.pyplot as mp;

conskey = 'CONSUMER_KEY'
cons_secret = 'SECRET CONSUMER_KEY'
authkey = 'AUTHENTICATION KEY'
authkey_secret = 'SECRET AUTH_KEY'

auth = tweepy.OAuthHandler(conskey, cons_secret)
auth.set_access_token(authkey, authkey_secret)
api = tweepy.API(auth)

username = input("Enter a username:")
user = api.get_user(screen_name=username)
 

followers_count = user.followers_count
tweets_count = user.statuses_count
print(f"{username} has {followers_count} followers and tweeted {tweets_count} times.")
print(f"name:{user.name} , desc: {user.description}, followers:{user.followers_count}, verified:{user.verified}")

 
username=input("enter other username:")
user2=api.get_user(screen_name=username)

xval = [user.name,user2.name]
yval = [user.followers_count, user2.followers_count]
fig = mp.figure(figsize = (10, 5))

mp.bar(xval, yval, color='blue', width=0.4)
mp.xlabel("Name")
mp.ylabel("No Of Followers")
mp.title("Followers analyser")
mp.show()







 
