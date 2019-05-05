# use natural language toolkit


import nltk
import random
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()

Greeting_response =["Hey" , "Hii :)" , "Hello Welcome !" , "Hi How may i help you ?" ,"Hi hope you are having a good day " , "Wassup ?" , "Hello"]
# 3 classes of training data
training_data = []

training_data.append({"class":"greeting", "sentence":"hi how are you? hello"})
training_data.append({"class":"greeting", "sentence":"ssup how is your day? wassup wasup"})
training_data.append({"class":"greeting", "sentence":"good day sup"})
training_data.append({"class":"greeting", "sentence":"how is it going today great hiii?"})

training_data.append({"class":"etl", "sentence":"run this feed id  etl pbus? timeseries composite"})
training_data.append({"class":"etl", "sentence":"get  account details feed  ipb exgeneva"})
training_data.append({"class":"etl", "sentence":"composite account timeseries  account "})
training_data.append({"class":"etl", "sentence":" type of account  composite model timeseries"})

training_data.append({"class":"pbus", "sentence":"account detials account exception"})
training_data.append({"class":"pbus", "sentence":"account exception count account pbus"})
training_data.append({"class":"pbus", "sentence":"closed exception count account"})
training_data.append({"class":"pbus", "sentence":"evaluation date account total details"})

training_data.append({"class":"cr", "sentence":"trigger  process   report"})
training_data.append({"class":"cr", "sentence":"generate reports  client"})
training_data.append({"class":"cr", "sentence":"generate reports  month"})
training_data.append({"class":"cr", "sentence":"page   report generated"})
print ("%s sentences of training data" % len(training_data))

# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our training data
for data in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(data['sentence']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # add the word to our words in class list
            class_words[data['class']].extend([stemmed_word])

# we now have each stemmed word and the number of occurances of the word in our training corpus (the word's commonality)
print ("Corpus words and counts: %s " % corpus_words)
# also we have all words in each class
print ("Class words: %s \n" % class_words)


# calculate a score for a given class taking into account word commonality
def calculate_class_score_acc(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score


# return the class with highest score for sentence
def classify(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of sentence for each class
        score = calculate_class_score_acc(sentence, c, show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score

