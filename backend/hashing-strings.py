import hashlib
import re
import requests
import json

API_URL = "http://127.0.0.1:8000"

"""


REWRITE THESE IN JS


"""


#all private methods below here
#hash the passed in text returning a hexdigest of md5
def hashText(passedText):
    hashObject = hashlib.md5(passedText.encode('utf-8')).hexdigest()
    return hashObject

#remove all whitespce from the document
def removeWhiteSpace(textFile: str):
    return textFile.replace(" ", "")

#Find all nouns in the file and remove them
def removeNouns(textFile: str):
    #find locations of all capital letters in the text
    returnString = textFile

    #look for all captial letters at the start of sentences
    words = re.findall("(?<!^)(?<!\. )[A-Z][a-z]+", returnString)
    print(words)
    
    for x in words:
        #wordIndex = textFile.find
        #length = x.length
        returnString = returnString.replace(x, '')

    return returnString



"""


DONT WORRY ABOUT BELOW HERE


"""


#open the file in read mode
def getFileText(filename):
    fileObj = open(filename, "r")
    return fileObj.read()

#get user input from console
def getUserInput():
    return input("Enter a string to hash")


#works
def doesHashExist(hashString: str):
    try:
        hashReq = requests.get(API_URL + "/api/hashes/" + hashString)
        #if not found returned
        if (hashReq.status_code == 404):
            print("Bad request 404 received")
            return False

        returnedJson = hashReq.json()
        returnedHashString = returnedJson["hashValue"]

        #return true if the returned string and passed in string are equal to eachother
        return (returnedHashString == hashString)
        
    except:
        return False
    
#works
def addHashToDB(hashString: str):
    try:
        jsonObj = {"hashValue": hashString}
        print(jsonObj)
        hashReq = requests.post(API_URL + "/api/hashes/", data=jsonObj)

        if (hashReq.status_code == 201):
            return True
        else:
            print("Adding new hash failed")
            print(hashReq.status_code)
            return False
    except:
        print("Adding new hash failed")
        return False

#updates the count for a string
def updateHashCount(hashString: str):
    try:
        hashReq = requests.get(API_URL + "/api/hashes/" + hashString)
        #if not found returned
        if (hashReq.status_code == 404):
            print("Bad request 404 received")
            return False

        returnedJson = hashReq.json()
        returnedHashString = returnedJson["hashValue"]
        #if the returned JSON already exists, add the count then update the counter in the db

        if (returnedHashString == hashString):
            returnedCounter = returnedJson["count"]
            newCounter = returnedCounter+1

            #create the updated object
            jsonObj = {"hashValue": hashString, "count": newCounter}
            #update the server
            
            hashReq = requests.put(API_URL + "/api/hashes/" + hashString + "/", data=jsonObj)
            if (hashReq.status_code==200):
                #hash count updated successfully
                print("Hash count updated successfully")
                return True
            else:
                print("Update failed")
                return False
        else:
            print("Update failed")
            return False
    except:
        return False
            

def getHashCount(hashString: str):
    try:
        hashReq = requests.get(API_URL + "/api/hashes/" + hashString)
        #if not found returned
        if (hashReq.status_code == 404):
            print("Bad request 404 received")
            return -1

        returnedJson = hashReq.json()
        returnedHashString = returnedJson["hashValue"]

        #return true if the returned string and passed in string are equal to eachother
        if (returnedHashString == hashString):
            return returnedJson["count"]
    
    except:
        return -1



#method to be called from JS
def processEmail(emailBody: str):
    """
    add or update email hash
    """
    #get the hash value from the body of the email
    hashValue = hashText(removeWhiteSpace(removeNouns(emailBody)))

    """
    redesign server
    /api/process/<hashstr>
    /api/retreive/<hashstr>
    """

    #if the email hash exists already on the database then increment the count
    #if the email hash does not exist then create a new record for the DB
    try:
        if (doesHashExist(hashString=hashValue)):
            return updateHashCount(hashString=hashValue)
        else:
            return addHashToDB(hashString=hashValue)
    except:
        print("An error occured")
        return False

#method to be called from js
def retreiveEmailDetails(emailBody: str):
    """
    return: number of times hash has been processed
    """
    #get the hash value from the body of the email
    hashValue = hashText(removeWhiteSpace(removeNouns(emailBody)))

    #search the database for an email string, if it does not exist return -1, if it does return the number of times it occurs
    try:
        return getHashCount(hashString=hashValue)
    except:
        return -1

    

#mainline
if __name__ == "__main__":
    """
    #get the number of times a specific thing occurs
    print(getHashCount("Stephen like COCK"))
    """
    """
    #update a hash count in a db
    print(updateHashCount("Stephen like COCK"))
    """

    """
    #test adding a new hash to the api
    print(addHashToDB("Stephen like COCK"))
    """

    
    #for checking if a hash exists in the db
    #unsuccessful request
    #print(doesHashExist("dsajdh"))
    #print("")
    #successful request
    #print(doesHashExist("agdhsjadyeuuw7823"))
    

    #testing hashing algorithm
    """
    email1 = getFileText("email1.txt")
    email2 = getFileText("email2.txt")

    email1hash = hashText(removeWhiteSpace(removeNouns(email1)))
    email2hash = hashText(removeWhiteSpace(removeNouns(email2)))

    print(email1hash == email2hash)
    print(email1hash)
    print(email2hash)
    """


    

#FURTHER ADVANCEMENT
#FIND A WAY FOR IT TO ALLOW NAMES AT THE START OF SENTENCES