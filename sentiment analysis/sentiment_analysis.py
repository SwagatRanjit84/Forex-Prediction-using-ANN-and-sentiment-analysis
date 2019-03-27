from initial_new import line
import initial_new as inew
import csv
from nltk.stem import PorterStemmer
ps=PorterStemmer()

testing=[]
category_prob={}
dictionary={}
diction={}
dictionary_word_count={}
final_dict={}
total_features=[]
pos=[]
neg=[]
feature_list=[]
with open("positive.csv", 'r') as file:
    posi= list(csv.reader(file))
with open("negative.csv", 'r') as file:
    nega= list(csv.reader(file))
for i in posi:
    po=ps.stem(*i)
    pos.append(po)
for j in nega:
    ne=ps.stem(*j)
    neg.append(ne)
with open("afinn.csv", 'r') as file:
    afinn= list(csv.reader(file))
mapp={}
afinn_words=[]
for i in range(len(afinn)):
    afin=ps.stem(afinn[i][0])
    afinn_words.append(afin)
    mapp[afin] =afinn[i][1]




# neg_words=["not","n't"]
neg_words=["not","n't","none","nobody","nothing","neither","nowhere","never"]

total_dict={}
def Naive_Bayes():
    count=0
    for i in range(len(line)):

        processed_tweet=inew.processTweet(line[i][1])
        count=count+1
        positive_class,negative_class=inew.getFeatureVector(processed_tweet,line[i][0])

    feature_list=positive_class+negative_class



    diction[0] = negative_class
    diction[1]=positive_class
    for i in diction:
        count = {}
        category_prob[i]=cat_prob(line,i)
          #word prob
        for j in diction[i]:
            count[j] = diction[i].count(j)
        dictionary[i]=count
    #test

    test(text,diction,feature_list,dictionary)

def word_prob(i,word,word_value,length,feature_list):
    feature_length=len(feature_list)
    if(word_value==0):
        getscore=0

        if(word in afinn_words):
            getscore=mapp[word]
            if(int(getscore)<0):
                symbol=0
            elif(int(getscore)>0):
                symbol=1
            if(symbol==i and symbol==0):
                word_value=int(getscore)*(-1)
            if(symbol==i and symbol==1):
                word_value=int(getscore)
            length=int(length)+1
            feature_length=(len(feature_list))+1



    words_probability = (word_value +1) / (int(length) + feature_length)


    word_probability=words_probability*1000



    return(word_probability)


#overall tweets
with open("overalltweets.csv", 'r') as file:
    line= list(csv.reader(file))

#tweetwolabels

with open("tweetwolabels.csv", 'r') as file:
    text= list(csv.reader(file))


def test(text,diction,feature_list,dictionary):
    county = 0
    for u in range(len(text)):#line

        oneline=text[u][0]


        negation=0
        processed_test_Tweet = inew.processTweet(oneline)

        words =processed_test_Tweet.split()
        for v in neg_words:
                for i in words:
                    if (v in i):


                        negation=negation+1

        if negation>0:
                    count_not = neg_count(processed_test_Tweet)

                    sentence_prob = testing_cal(processed_test_Tweet, diction, feature_list, dictionary)

                    if (count_not % 2 == 0 ):
                        if (sentence_prob[0] > sentence_prob[1]):


                            testing.append(0)

                        elif (sentence_prob[0] < sentence_prob[1]):

                            testing.append(int(1))
                    else:
                        if (sentence_prob[0] > sentence_prob[1]):

                              testing.append(int(1))

                        elif (sentence_prob[0] < sentence_prob[1]):

                              testing.append(0)

        else:
               sentence_prob=testing_cal(processed_test_Tweet, diction, feature_list, dictionary)
               if (sentence_prob[0] > sentence_prob[1]):
                    testing.append(0)

               elif (sentence_prob[0] < sentence_prob[1]):
                    testing.append(int(1))



    calculate(processed_test_Tweet)

def test_user(line,diction,feature_list,dictionary):
   # line
        negation = 0
        processed_test_Tweet = inew.processTweet(line)
        words = processed_test_Tweet.split()
        for v in neg_words:
            for i in words:
                if (v in i):
                    negation = negation + 1

        if negation > 0:
            count_not = neg_count(processed_test_Tweet)
            print(count_not)


            sentence_prob = testing_cal(processed_test_Tweet, diction, feature_list, dictionary)
            if(count_not%2==0):
                print(sentence_prob[0])
                print(sentence_prob[1])
                if (sentence_prob[0] >sentence_prob[1]):
                    testing.append(int(0))
                    print("negative")
                elif (sentence_prob[0] < sentence_prob[1]):
                    print("m not 0")
                    testing.append(int(1))
                    print("positive")
            else:
                if (sentence_prob[0] > sentence_prob[1]):
                    testing.append(int(1))
                    print("positive")
                elif (sentence_prob[0] < sentence_prob[1]):
                    testing.append(0)
                    print("negative")
        else:
            sentence_prob = testing_cal(line, diction, feature_list, dictionary)
            if (sentence_prob[0] > sentence_prob[1]):
                testing.append(0)
                print("negative")
            elif (sentence_prob[0] < sentence_prob[1]):
                testing.append(int(1))
                print("positive")

            else:
                print("the given sentence cannot be clasiified by our model:")

        a = input("again?")
        if (a == "y" or "Y"):
            test_line = input("enter sentence--")
            test_user(test_line, diction, feature_list, dictionary)
        else:
            print("have a good day")


def testing_cal(u,diction,feature_list,dictionary):
        oneline = replace_neg(u)


        feature_test=inew.get_test_feature(oneline)

        sentence_prob={}
        for i in diction:

            probability_sentence = 1
            cat=category_prob[i]
            countos=0
            for w in feature_test:
                if w in diction[i]:
                    countos=countos+1
            z=0
            for w in feature_test:
                    z=z+1


                # if w not in feature_list:
                #     continue
                # else:
                    if w not in diction[i]:
                        word_value = 0

                    elif w in diction[i]:
                        word_value = dictionary[i].get(w)


                    length=len(diction[i])

                    word_probaility=word_prob(i,w,word_value,length,feature_list)
                    if(countos==0 ):

                        word_probaility=0



                    probability_sentence=probability_sentence*word_probaility




            total_probability=probability_sentence*cat

            sentence_prob[i]=total_probability

        if(((sentence_prob[0]==cat_prob(line,0)) and (sentence_prob[1]==cat_prob(line,1))) or (sentence_prob[0]==0 and sentence_prob[1]==0)):
            polarity=0

            for one_word in feature_test:


                if one_word in afinn_words:
                    b=mapp[one_word]

                else:
                    b=0
                polarity=polarity+int(b)

            if(polarity>0):
                sentence_prob[1]=1
                sentence_prob[0]=0
            elif(polarity<0):
                sentence_prob[0]=1
                sentence_prob[1]=0


        return sentence_prob

def replace_neg(line):
    words = line.split()

    for w in words:
        for n in neg_words:

            if (w.count(n)!=0):

                line = line.replace(n, " ")

                line = " ".join(line.split())
    return line


def cat_prob(line,i):
    count=0
    for one_line in line:
        if int(one_line[0])==i:
            count=count+1
        else:
            continue
    return count/len(line)

#calculating
#tweetwithlabels
a=[]
with open("tweetwithlabels.csv", 'r') as file:
    tests_text= list(csv.reader(file))


def calculate(u):
    tests_original=[]
    counti=0
    for i in tests_text:
        tests_original.append(int(i[0]))

    true_negative=0
    true_positive=0
    false_negative=0
    false_positive=0
    for i in tests_original:

        if(i==1):
            if(tests_original[counti]==testing[counti]):
                true_positive=true_positive+1

            else:
                false_negative=false_negative+1

        if(i==0):
            if(tests_original[counti]==testing[counti]):
                true_negative=true_negative+1

            else:
                false_positive=false_positive+1

        counti = counti + 1
    print(tests_original)
    print(testing)
    calculate_prf(tests_original,true_positive,true_negative,false_positive,false_negative)



def calculate_prf(test_original,tp,tn,fp,fn):
    pos_precision=tp/(tp+fp)
    neg_precision=tn/(tn+fn)
    pos_recall=tp/(tp+fn)
    neg_recall=tn/(tn+fp)
    counting=0

    for u in range(len(text)):#line

        oneline=text[u][0]

        processed_test_Tweet = inew.processTweet(oneline)
        b=test_original[counting]
        c=testing[counting]
        if(b==0):
            x="negative"
        elif(b==1):
            x="positive"
        if(c==0):
            y="negative"
        elif(c==1):
            y="positive"





        print(processed_test_Tweet)
        print("actual--",x)
        print("predicted--",y)
        counting=counting+1


    print("pos_precision")
    print(pos_precision)
    print("neg_precision")
    print(neg_precision)
    print("pos_recall")
    print(pos_recall)
    print("neg_recall")
    print(neg_recall)
    accuracy=(tp+tn)/(tp+fp+tn+fn)
    print("accuracy")
    print(accuracy)
    pos_F=(2*pos_precision*pos_recall)/(pos_precision+pos_recall)
    neg_F=(2*neg_precision*neg_recall)/(neg_precision+neg_recall)
    print("pos_F")
    print(pos_F)
    print("neg_F")
    print(neg_F)



    import numpy as np
    import matplotlib.pyplot as plt


    x=[0,5,10,15,20,25,30]
    plt.subplot(2, 1, 1)
    plt.title('actual trends')
    plt.stem(test_original)
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))


    plt.subplot(2, 1, 2)
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))


    plt.title('predicted trends')

    plt.stem(testing)
    plt.show()




def neg_count(str):
    aa=0
    for nega in neg_words:
        aa=aa+str.count(nega)


    return aa

Naive_Bayes()





