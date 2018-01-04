import fetchTWEETS
import tokeniser

print('Collection of tweets started... It might take a few minutes \n')
fetchTWEETS.testrun()
print('Tweets & hashtag collection completed \n')

print('Tokenisation of tweets initiated .....')
tokeniser.tokeniser_self_func()
print('Tokenisation of tweets completed. Output in tokenised_tweets.txt \n\n Further Instructions\n\n 1) Run map reduce jobs using hashtags.txt - python-script hashtag_count.py and tokenised_tweets.txt - python script word_count.py. \n 3) The output file of map reduce hastags count job should be named hashtagsCounted.txt & for tokenised tweets should be named englishwordCounted.txt \n 4) Now you can run top10_hastags.py and top10_english_words.py to get the most popular words. \n')
