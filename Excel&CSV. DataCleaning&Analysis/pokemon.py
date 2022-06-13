from collections import defaultdict
import csv

#reads raw CSV file and compiles (# of firetype pokemon >= level 40  /  total # of firetype pokemon)  
def fireRead():
    rows = []

    #opens CSV file and populates rows list with entries
    with open("pokemonTrain.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    

    totalcount = 0
    targetcount = 0
    
    #iterates through rows list
    for entry in rows:
        #increments totalcount if a pokemon is a firetype
        if "fire" in entry[4]:
            totalcount += 1
            #print(entry)

            #increment targetcount if firetype pokemon is >= level 40
            if float(entry[0]) >= 40:
                targetcount +=1

    ansTotal = float(totalcount)
    ansTarget = float(targetcount)
    #print(ansTarget)
    #print(ansTotal)

    #rounds answer to nearest integer
    ans = ansTarget/ansTotal
    ans = ans*100
    #print(ans)
    ans = round(ans)
    #print(ans)
    

    #construct string to write to text file
    with open('pokemon1.txt', 'w') as f:
        f.write("Percentage of fire type Pokemons at or above level 40 = "+str(ans))

def missingtype():
    rows = []
    #opens CSV file and populates rows list with entries
    with open("pokemonTrain.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    for entry in rows:
        #print(entry)
        if "NaN" in entry[4]:
            #print(entry)
            ans = searchWeakness(rows, entry[5])
            entry[4] = ans
    # for index, entry in enumerate(rows):
    #     print(str(index)+" "+str(entry))
    
    return rows


def missingstats(list):
    # ab = []
    # be = []

    # for entry in list:
    #     if int(entry[2]) > 40:
    #         ab.append(entry)
    #     else:
    #         be.append(entry)

    # for index, entry in enumerate(ab):
    #     print(str(index)+" "+str(entry))

    for entry in list:

        if float(entry[2]) > 40:
            for i in range(6,9):
                if "NaN" in entry[i]:
                    ans = avgstatcollumn(list, i, "above")
                    entry[i] = str(ans)
        else:
            for i in range(6,9):
                if "NaN" in entry[i]:
                    ans = avgstatcollumn(list, i, "below")
                    entry[i] = str(ans)
    
    # for index, entry in enumerate(list):
    #     print(str(index) + " " + str(entry))
    
    with open("pokemonResult.csv", "w",  newline="") as f:
        writer = csv.writer(f)

        for entry in list:
            
            writer.writerow(entry)
    
def populateDict():
    rows = []
    dict = defaultdict(list)
    #opens CSV file and populates rows list with entries
    with open("pokemonResult.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)

    for entry in rows:
        if entry[4] not in dict:
            dict[entry[4]].append(entry[3])
        else:
            if entry[3] not in dict[entry[4]]:
                dict[entry[4]].append(entry[3])
        
    
    
    d2 = {x:sorted(dict[x]) for x in dict.keys()}
    d2 = sorted(d2.items())
    with open('pokemon4.txt', 'w') as f:
        f.write("Pokemon type to personality mapping:")
        f.write("\n")

        f.write("\n")
        for key, value in d2:
            f.write("\t")
            f.write(key+": ")
            str = ""
            for item in value:
                str += item
                str += ", "
            str = str.rstrip(" ")
            str = str.rstrip(",")
            f.write(str)
            f.write("\n")
           

def avgHP():
    rows = []
    with open("pokemonResult.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            rows.append(row)
    curr = 0
    total= 0
    for entry in rows:
        if float(entry[9]) == 3:
            curr += float(entry[8])
            total += 1
            
    # print(curr)
    # print(total)
    ans = float(curr/total)
    ans = round(ans,1)
    #print(ans)
    with open("pokemon5.txt", "w") as f:
        f.write("Average hit point for Pokemons of stage 3.0 = "+str(ans))



#searches corresponding collumn for type
def searchWeakness(list, str):
    dict = {}
    
    for entry in list:
        if str in entry[5]:
            if "NaN" in entry[4]:
                a= 0

            else:
                if entry[4] not in dict:
                    dict[entry[4]] = 1
                else:
                    dict[entry[4]] += 1

    #print(dict)
    max_value = max(dict.values())  # maximum value
    max_keys = [key for key, value in dict.items() if value == max_value] # getting all keys containing the `maximum`
    max_keys.sort()
    #print(max_keys)
    return max_keys[0]

def avgstatcollumn(list, i, gate):
    val = 0
    total = 0
    


    if "above" in gate:
        for entry in list:
            if float(entry[2]) > 40:
                if "NaN" in entry[i]:
                    a = 0
                else:
                    val += float(entry[i])
                    total += 1
                #print(entry)
        # print(i)
        # print(val
        # print(total)
        ans = float(val/total)
        ans = round(ans, 1)
        return ans
    else:
        for entry in list:
            if float(entry[2]) <= 40:
                if "NaN" in entry[i]:
                    a = 0
                else:
                    val += float(entry[i])
                    total += 1
                #print(entry)
        # print(i)
        # print(val)
        # print(total)
        ans = float(val/total)
        ans = round(ans, 1)
        return ans

if __name__ == "__main__":
    fireRead()
    newlist = missingtype()
    missingstats(newlist)
    populateDict()
    avgHP()
    
