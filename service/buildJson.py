from dateutil.parser import parse

def is_date(string, fuzzy=True):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def getInfo(sentence):
    if(is_date(sentence)==False):
        print('We would like to know the Date')
        dateInput=input('Date (MM-DD-YYYY) :')
        getInfo(dateInput)
    else:
        print('Date Found will build the json ')
        return 'Received'


#sentence1=input()
#getInfo(sentence1)

"""    
Need to pass a dictionary which will have all the parameter    
def buildCmpJson(sentence):    
    return '{serviceId: '+sentence+'}'
"""