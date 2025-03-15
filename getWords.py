from meta_ai_api import MetaAI

def getParragraph():
    ai = MetaAI()
    response = ai.prompt(message='Generate a single paragraph for a typing game. The paragraph should be diverse in topic and contain a variety of ideas, such as a mix of nature, technology, and human experience. The language should be descriptive but not too complex, and the text to be typed should be placed inside quotes.')

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
