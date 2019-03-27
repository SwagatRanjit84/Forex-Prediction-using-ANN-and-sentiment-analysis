import csv
import re
from nltk.stem import PorterStemmer
import matplotlib as m
ps=PorterStemmer()


with open("overalltweets.csv", 'r') as file:
    line= list(csv.reader(file))



#start process_tweet
def processTweet(tweet):
    # process the tweets
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+',' ',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet

#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList():
    #read the stopwords file and build a.csv list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open('stopwords', 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()

    return stopWords
#end

feature_list=[]
positive_class=[]
negative_class=[]

#start getfeatureVector
def getFeatureVector(tweet,score):

    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:


        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        stopWords=getStopWordList()

        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word

        if(w in stopWords or val is None):
             continue
        else:

            stemer=ps.stem(w)

        if score==str("1"):
            positive_class.append(stemer)

        elif score==str("0"):
                negative_class.append(stemer)
        else:
                print("error----------------------")


    return positive_class,negative_class
#end

def get_test_feature(processed_test):



    feature_test = []
    # split tweet into words
    words = processed_test.split()

    stopWords=getStopWordList()

    for w in words:

        # replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        # strip punctuation
        w = w.strip('\'"?,.')

        # check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        # ignore if it is a stop word
        if (w in stopWords or val is None):

            continue
        else:
            stemer = ps.stem(w)
            feature_test.append(stemer)

    return feature_test


def get_total_classes(positive,negative):
    positive_stem=[]
    negative_stem=[]
    with open("negative.csv", 'r') as file:
        neg = list(csv.reader(file))
    with open("positive.csv", 'r') as file:
        pos = list(csv.reader(file))
    posi = []
    negi = []
    for i in pos:
        posi.append(*i)
    for j in neg:
        negi.append(*j)

    for i in posi:
        positive_stem.append(ps.stem(i))
    for j in negi:
        negative_stem.append(ps.stem(j))


    pos_optimize=list(set(positive_stem))
    neg_optimize=list(set(negative_stem))

    positive_class=positive+pos_optimize
    negative_class=negative+neg_optimize



    return positive_class,negative_class

