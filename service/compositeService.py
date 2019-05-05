from service.buildJson import *


def compositeService(sentence):
        print("Message receiveced - "+sentence)
        etlJson = getInfo(sentence)
        return '{ '+etlJson.__str__()+' }'
