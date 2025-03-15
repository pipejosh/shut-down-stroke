from meta_ai_api import MetaAI

def getParragraph():
    ai = MetaAI()
    response = ai.prompt(message='give me a parragraph of words for a typing game')

    return response['message']

def filteresResponse():

    response = getParragraph()
    responseFilteres = ""
    inMessage = False

    for i in response:

        if i == '"':
            inMessage = not inMessage

        if inMessage:
            responseFilteres += i 
    
    responseFilteres = responseFilteres.replace('"', '')

    return responseFilteres

def getWords():
    filteredWords = filteresResponse()
    words = filteredWords.split();
    return words
