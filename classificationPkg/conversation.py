from classificationPkg.classification import classify, class_words , Greeting_response , calculate_class_score_acc
from service.compositeService import compositeService

import random



print("\n\033[1;30;47m SmartBot: Welcome to Smart Bot !!")
#print("\n\033[1;32;40m SmartBot Ready to help you :)  !!\n")
while True:
    sentence = input("\033[1;32;0m You: ")
#    for c in class_words.keys():
#        print ("Class: %s  Score: %s \n" % (c, calculate_class_score_acc(sentence, c)))
    prediction=[]
    prediction=classify(sentence)
    if prediction[0] == "greeting":
        print("\033[1;32;0m SmartBot: "+random.choice(Greeting_response))
    elif prediction[0] == "etl":
        print("\033[1;32;0m SmartBot: Our understanding is you want to trigger a ETL")
        cmpResponse=compositeService(sentence)
        print(cmpResponse)
    elif prediction[0] == "cr":
        print("\033[1;32;0m SmartBot: Our understanding is you want to generate a report")
    elif 'bye' in sentence:
        print("\033[1;32;0m SmartBot: Goodbye Have a Nice day!  \n")
        break
    else:
        print("\033[1;32;0m SmartBot: I am not able to understand , can you provide more details")

