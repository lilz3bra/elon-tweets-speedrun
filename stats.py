import csv

rows = []
with open("elon.csv", encoding='utf-8') as f:
    csvr = csv.reader(f)
    header = next(csvr)
    for row in csvr:
        rows.append(row)

allwords = 0

for i in range(2010, 2022):
    count = 0
    words = 0
    string = f'{i} \t'
    for r in rows:
        if str(i) in r[2] and r[31] == '[]':
            count += 1
            allwords += len(r[10].split())
            words += len(r[10].split())
    print(f"Year: {i}  Tweets: {count}  Avg words: {round(words/count, 2)}")
print(f"Total words: {allwords}")