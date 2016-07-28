from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Twitter credentials.Get them from https://apps.twitter.com
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACESS_TOKEN=""
ACCESS_TOKEN_SECRET=""

class listener(StreamListener):    
    def on_data(self,data):
        #print data
        tweet=data.split('''"text":"''')[1].split('''","source"''')[0]
        print tweet
        sent=sum(map(lambda word:wordDB.get(word,0),tweet.lower().split()))
        print sent
        fh=open("twitterdata.csv",'a')
        fh.write(tweet)
        fh.write('\n')
        fh.write("Sentimental Score: "+str(sent)+"\n")
        fh.write("=======================================================================================================")
        fh.write("\n")         
        fh.close()
        return True
        
    def on_error(self,status):
        print status

auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

wordDB=dict(map(lambda (k,v):(k,int(v)),[line.split('\t') for line in open("vocabDB.txt")]))

twitterStream=Stream(auth,listener())
### Enter the tags you want to search the tweets about. 
twitterStream.filter(track=["<Enter tags here>"],languages=["en"])

    
