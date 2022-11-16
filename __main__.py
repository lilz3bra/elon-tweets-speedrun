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
        'reply_to': r[31]
    }
    if tempdict['reply_to'] == '[]':
        ttweetList.append(int(tempdict['id']))
ttweetList.sort()
for t in ttweetList:
    tweetList.append(str(t))
with open("elon.json", "w+") as o:
    json.dump(tweetList, o)
