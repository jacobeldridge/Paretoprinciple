import random
import csv
import pandas as pd
import matplotlib.pylab as plt
import collections

chars = 'abcdefghijklmnopqrstuvwxyz'
words = ['']
wordcounter = {}
rand = random.randint(1, 27)
count = 0
times = input("how many words do you want?")
times = int(times)
while times != len(words):
    if rand != 27 or words[-1] == '':
        words[-1] = words[-1] + random.choice(chars)
        print(len(words))
        rand = random.randint(1, 27)
    else:
        words.append("")
        rand = random.randint(1, 27)
    count += 1
words.pop(-1)
for i in words:
    if i not in wordcounter:
        wordcounter[i] = 1
    else:
        wordcounter[i] += 1

print(wordcounter)
sorted_x = sorted(wordcounter.items(), key=lambda kv: kv[1], reverse=True)
sorted_dict = collections.OrderedDict(sorted_x)
df = pd.DataFrame.from_dict(sorted_dict, orient='index')
# sorted_df = df.sort_values(by="0")
df.to_csv("zyph.csv")
# print(sorted_df)
        
        