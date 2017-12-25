import codecs
from nltk.tokenize import *
""" emoticon recognition via patterns.  tested on english-language twitter, but
probably works for other social media dialects. """

__author__ = "Brendan O'Connor (anyall.org, brenocon@gmail.com)"
__version__= "april 2009"

#from __future__ import print_function
import re,sys

mycompile = lambda pat:  re.compile(pat,  re.UNICODE)
SMILEY = mycompile(r'[:=].{0,1}[\)dpD]')
MULTITOK_SMILEY = mycompile(r' : [\)dp]')

NormalEyes = r'[:=]'
Wink = r'[;]'

NoseArea = r'(|o|O|-)'   ## rather tight precision, \S might be reasonable...

HappyMouths = r'[D\)\]]'
SadMouths = r'[\(\[]'
Tongue = r'[pP]'
OtherMouths = r'[doO/\\]'  # remove forward slash if http://'s aren't cleaned

Happy_RE =  mycompile( '(\^_\^|' + NormalEyes + NoseArea + HappyMouths + ')')
Sad_RE = mycompile(NormalEyes + NoseArea + SadMouths)

Wink_RE = mycompile(Wink + NoseArea + HappyMouths)
Tongue_RE = mycompile(NormalEyes + NoseArea + Tongue)
Other_RE = mycompile( '('+NormalEyes+'|'+Wink+')'  + NoseArea + OtherMouths )

Emoticon = (
    "("+NormalEyes+"|"+Wink+")" +
    NoseArea + 
    "("+Tongue+"|"+OtherMouths+"|"+SadMouths+"|"+HappyMouths+")"
)
Emoticon_RE = mycompile(Emoticon)

#Emoticon_RE = "|".join([Happy_RE,Sad_RE,Wink_RE,Tongue_RE,Other_RE])
#Emoticon_RE = mycompile(Emoticon_RE)
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
	u"\U0001F600-\U0001F644"
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def analyze_tweet(text):
  text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
  text = Emoticon_RE.sub(' ',text)
  text = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)
  text = SMILEY.sub(' ',text)
  text = MULTITOK_SMILEY.sub(r'',text)
  text = emoji_pattern.sub(r'', text)
  
  s= Sad_RE.search(text)
  #if h and s: return "BOTH_HS"
  #if h: return "HAPPY"
  #if s: return "SAD"
  return text

  # more complex & harder, so disabled for now
  #w= Wink_RE.search(text)
  #t= Tongue_RE.search(text)
  #a= Other_RE.search(text)
  #h,w,s,t,a = [bool(x) for x in [h,w,s,t,a]]
  #if sum([h,w,s,t,a])>1: return "MULTIPLE"
  #if sum([h,w,s,t,a])==1:
  #  if h: return "HAPPY"
  #  if s: return "SAD"
  #  if w: return "WINK"
  #  if a: return "OTHER"
  #  if t: return "TONGUE"
  #return "NA"




tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
f = codecs.open('tweets.txt', 'r', encoding="utf-8-sig")
alllines = list()
for line in f:
    alllines.append(tknzr.tokenize(analyze_tweet(line)))
    #alllines.append(tknzr.tokenize(re.sub("^\d+\line|\line\d+\line|\line\d+$", " ", analyze_tweet(line))))
    #alllines.append(re.sub("^\d+\line|\line\d+\line|\line\d+$", " ", analyze_tweet(line)))
    
nufile= open('tokenised_data.txt','w')
# print(alllines)
for ln in alllines:
    for i in ln:
        nufile.write(i)
        nufile.write('\n')

