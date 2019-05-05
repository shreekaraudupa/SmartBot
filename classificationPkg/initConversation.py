from classificationPkg.classification import classify, class_words , Greeting_response , calculate_class_score_acc
from service.compositeService import compositeService

import random

print("\n\033[1;30;47m SmartBot: Welcome to Smart Bot !!")

while True:
    sentence = input("\033[1;32;0m You: ")
#    for c in class_words.keys():
#        print ("Class: %s  Score: %s \n" % (c, calculate_class_score_acc(sentence, c)))
    prediction=[]
    prediction=classify(sentence)
    if prediction[0] == 'greeting':
        print("\033[1;32;0m SmartBot: "+random.choice(Greeting_response))
    elif prediction[0] == 'etl':
        check = input("SmartBot: Our understanding is you want to trigger a ETL? y/n")
        if check.lower() == 'y':
            cmpResponse=compositeService(sentence)
            print(cmpResponse)
        else:
            print("SmartBot: Please enter your request again ")
    elif prediction[0] == 'cr':
        print("\033[1;32;0m SmartBot: Our understanding is you want to generate a report")
    elif 'bye' in sentence:
        print("\033[1;32;0m SmartBot: Goodbye Have a Nice day!  \n")
        break
    elif prediction[0] == 'pbus':
        print('SmartBot: Getting all the required details from SQL')
    else:
        print("\033[1;32;0m SmartBot: I am not able to understand , can you provide more details")

