import json
import csv


rows = []
with open("elon.csv", encoding='utf-8') as f:
    csvr = csv.reader(f)
    header = next(csvr)
    for row in csvr:
        rows.append(row)

tweetList = []
ttweetList = []
for r in rows:
    tempdict = {
        'id': r[0],
        'created_at': r[2], 
        'tweet': r[10], 
        'mentions': r[12], 'urls': r[13], 'photos': r[14], 
        'replies_count': r[15], 'retweets_count': r[16], 'likes_count': r[17], 
        'hashtags': r[18], 'cashtags': r[19], 'link': r[20], 'retweet': r[21], 
        'quote_url': r[22], 'video': r[23], 'thumbnail': r[24], 'reply_to': r[31]
    }
    if tempdict['reply_to'] == '[]':
        ttweetList.append(int(tempdict['id']))


# print(header)
ttweetList.sort()
for t in ttweetList:
    tweetList.append(str(t))
with open("elon.json", "w+") as o:
    json.dump(tweetList, o)
print(len(tweetList))
