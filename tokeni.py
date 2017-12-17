from nltk.tokenize import *
tknzr = TweetTokenizer()
f = open('tweets.txt', 'r')
alllines = list()
for line in f:
    alllines.append(tknzr.tokenize(line))


for ln in alllines:
    print(ln)
    print('\n')
