from meta_ai_api import MetaAI
import random

def getParragraph():

    randomNumber = random.randint(0, 12)
    ai = MetaAI()
    topics = [
        "Global history",
        "Technology advancements",
        "The future of entertainment",
        "Space exploration",
        "Environmental issues",
        "Psychology and human behavior",
        "The future of artificial intelligence",
        "Global economy and trade",
        "The future of transportation",
        "Medical discoveries and healthcare",
        "Cultural diversity and anthropology",
        "The future of education",
        "Moral and ethical dilemmas",
    ]

    response = ai.prompt(message=f"Write a paragraph about {topics[randomNumber]}. Please enclose the paragraph in quotes. Respond with the text in quotes only.")
    
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
