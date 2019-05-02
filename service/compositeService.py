from service.buildJson import *


def compositeService(sentence):
    check=input("SmartBot: Is our prediction right ? y/n")
    if check.lower() == 'y':
        print("Message receiveced - "+sentence)
        etlJson = getInfo(sentence)
        return etlJson
    else:
        print("Its not ETL please enter your request again ")
        return False
