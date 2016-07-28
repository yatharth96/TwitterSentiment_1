from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

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
        fh.write("======================================================================================")
        fh.write("\n")         
        fh.close()
        return True
        
    def on_error(self,status):
        print status

auth=OAuthHandler("TiSNgNuLqwJ6zizM6uuC1ggOg","qrwe5VNUevtrU0t9lvlv0z6w9J97PNosHQ9O8Orn9yFf0EdsYZ")
auth.set_access_token("443542132-SM0FVcmbabPyTFmf8Fi0BfCCfV5Nbyblm39hT2sB","3fEcym0sP3UtnhkhIVvgEGf5zbC646S9B1dDSaFL9doi2")

wordDB=dict(map(lambda (k,v):(k,int(v)),[line.split('\t') for line in open("AFINN-111.txt")]))

twitterStream=Stream(auth,listener())
twitterStream.filter(track=["Sultan"],languages=["en"])

    
