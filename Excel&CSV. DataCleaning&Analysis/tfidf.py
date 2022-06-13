import math
import collections
import re
import csv
from typing import final

docAmount = 0

def cleanFile(fname):
    string = ""
    punct = re.compile("[^\w\s]")
    
    with open(fname, "r") as f:
        for entry in f:
            entry = re.sub(punct, "",entry)
            string += entry
            #string += "\n"
    #string = " ".join(string.split())
    pattern = re.compile('http[s]?[a-zA-Z0-9]*')
    string = pattern.sub('', string)
    string = " ".join(string.split())
    string = string.lower()
    stopList = []
    with open ("stopwords.txt", "r") as f:
        for entry in f:
            s1 = entry.strip()
            stopList.append(s1)

    #print(stopList)
    s1 = string.split(" ")
    i = 0
    final = ""
    while i < len(s1):
        if s1[i] not in stopList:
            final += s1[i]
            final += " "
        else: 
            final += ""
        i+=1
    suffixList = []
    suffixList.append("ing")
    suffixList.append("ly")
    suffixList.append("ment")
    #print(suffixList)
    for entry in suffixList:
        if entry in final:
            final = re.sub(entry, "", final)

    # print(string)
    # print("\n")
    #print(final)
    outName = "preproc_"
    outName += fname
    #print(outName)
    with open(outName, "w") as f:
            f.write(final)

def calculateTFIDF(total):
    dict= {}
    totalDict = {}
    list = []
    docuList = []

    with open("tfidf_docs.txt", "r") as file:
        for entry in file:
            entry = entry.strip()
            entry = entry.rstrip()
            docuList.append(entry)
            outName = "preproc_"
            outName += entry
            with open(outName, "r") as afile:
                for entry in afile:
                    entry = entry.strip()
                    entry = entry.rstrip()
                    list.append(entry)
                    
    for entry in list:
        for a in entry.split(" "):
            if a not in totalDict:
                totalDict[a] = 1
            else:
                totalDict[a] += 1

    count = 0  
    cnt = 0
    for entry in list:
        dict = {}
        for a in entry.split(" "):
            if a not in dict:
                dict[a] = 1
            else:
                dict[a] += 1
        
        newDict = {}
        
        for ent in dict:
            numinDoc = dict[ent]
            totalinDoc = termCount(dict)
            sepDocnum = inDoc(list, ent)
            if dict[ent] < totalDict[ent]:

                if ent not in newDict:
                    tf = float(numinDoc/totalinDoc)
                    idf = math.log(total/sepDocnum)
                    idf += 1
                    TfIdf = tf*idf
                    TfIdf = round(TfIdf, 2)
                    newDict[ent] = TfIdf

            else:
                if ent not in newDict:
                    tf = float(numinDoc/totalinDoc)
                    idf = math.log(total/1)
                    idf += 1
                    TfIdf = tf*idf
                    TfIdf = round(TfIdf, 2)
                    newDict[ent] = TfIdf


        #newDict = sorted(newDict.items(), key=lambda x: x[1], reverse=True)
        #newDict= sorted(newDict.keys(), key=lambda x:x.lower())
        popularWords = sorted(newDict, key = lambda x: (-newDict[x], x))
        i = 0
        if len(popularWords) > 5:
            while len(popularWords) != 5:
                popularWords.pop()
        
        
        finalList = []
        for entry in popularWords:
            finalList.append((entry, newDict[entry]))
            
        tempstring = "tfidf_"
        tempstring += docuList[cnt]
        
        with open(tempstring, "w") as TFIDFfile:
            TFIDFfile.write(str(finalList))

        cnt +=1


    
    # print("\n")
    # print(inDoc(list, "edited"))

def termCount(dict):
    count = 0
    for entry in dict:
        count += dict[entry]

    return count

def inDoc(list, term):
    count = 0
    for entry in list:
        for a in entry.split(" "):
            if term in a:
                count += 1
                break
    return count


if __name__ == "__main__":
    docAmount = 0
   
    with open ("tfidf_docs.txt", "r") as file:
        for entry in file:
            entry = entry.rstrip()
            cleanFile(entry)
            docAmount +=1
    
    calculateTFIDF(docAmount)
    
    
    
    