import math
import collections
import re
import csv
from collections import defaultdict

def cleanAge():
    rows = []

    try:
        #opens CSV file and populates rows list with entries
        with open("covidTrain.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
        
            for row in csvreader:
                rows.append(row)
    
    #print(header)
        for entry in rows:
            if "-" in entry[1]:
                string = entry[1].split("-")
                total = float(string[0]) + float(string[1])
                ans = float(total/2)
                ans = round(ans,1)
                #print(ans)
                entry[1] = ans
                # print(str[0] +" "+str[1])
                # print(total)
    except:
        print("Error Empty File")
    return rows

def cleanDate(list):
    for entry in list:
        str1 = entry[8].split(".")
        t1 = ""
        t1 += str1[1]
        t1 += "."
        t1 += str1[0]
        t1 += "."
        t1 += str1[2]
        entry[8] = t1

        str2 = entry[9].split(".")
        t2 = ""
        t2 += str2[1]
        t2 += "."
        t2 += str2[0]
        t2 += "."
        t2 += str2[2]
        entry[9] = t2

        str3 = entry[10].split(".")
        t3 = ""
        t3 += str3[1]
        t3 += "."
        t3 += str3[0]
        t3 += "."
        t3 += str3[2]
        entry[10] = t3
    
    return list

def cleanLatLong(list):
    # for index, entry in enumerate(list):
    #     print(str(index)+" "+entry[6]+" "+entry[7])

    for index, entry in enumerate(list):
        for i in range(6,8):
            if "NaN" in entry[i]:
                #print(index)
                ans = calculateProvince(list, i, entry[4])
                #print(ans)
                ans = round(ans, 2)
                #print(ans)
                entry[i] = str(ans)
    return list
    # for index, entry in enumerate(list):
    #     print(str(index)+" "+entry[6]+" "+entry[7])
    
def cleanCity(list):
    for index, entry in enumerate(list):
        if "NaN" in entry[3]:
            string = calculateCity(list, entry[4])
            #print(str)
            entry[3] = string
    
    return list

def cleanSymptoms(list):
    for entry in list:
        entry[11] = entry[11].replace(" ","")
    
    for index, value in enumerate(list):
        if "NaN" in value[11]:
            str = calculateSymptoms(list, value[4])
            value[11] = str

    with open("covidResult.csv", "w",  newline="") as f:
        writer = csv.writer(f)
        for entry in list:
            writer.writerow(entry)

def calculateSymptoms(list, province):
    str = ""
    dict = {}
    for entry in list:
        if province in entry[4]:
            if "NaN" not in entry[11]:
                str = entry[11]
                for ent in str.split(";"):
                    string = ent.strip()
                    if string not in dict:
                        dict[string] = 1
                    else:
                        dict[string] += 1

    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True) 
    list = []
    max = 0
    for key, value in dict:
        if value >= max:
            max = value
            list.append(key)
    list.sort()
    str = list[0]
    # print(province)
    # for entry in dict:
    #     print(entry)
    # print("List is: ")
    # print(list)
    # print(str)
    # print("\n")
    return str


def calculateCity(list, province):
    str = ""
    dict = {}
    for index, entry in enumerate(list):
        if province in entry[4]:
            if "NaN" not in entry[3]:
                if entry[3] not in dict:
                    dict[entry[3]] = 1
                else:
                    dict[entry[3]] += 1
                # print(index)
                # print(entry[3]+" "+entry[4]

  
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True) 
    list = []
    max = 0
    for key, value in dict:
        if value >= max:
            max = value
            list.append(key)
    # print(dict)
    # print("\n")
    list.sort()
    str = list[0]
    return str


def calculateProvince(list, i, province):
    count = 0
    total = 0
    
    for entry in list:
        if province in entry[4]:
            if "NaN" not in entry[i]:
                count += float(entry[i])
                total += 1

    ans = float(count/total)
    return ans


if __name__ == "__main__":
    l1 = cleanAge()
    l2 = cleanDate(l1)
    l3 = cleanLatLong(l2)
    l4 = cleanCity(l3)
    cleanSymptoms(l4)

