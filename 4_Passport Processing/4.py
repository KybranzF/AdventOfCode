#!/usr/bin/env python3.9

def validate(item):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if item[0] == "byr":
        # four digits
        if not len(item[1]) == 4:
            return 0
        #at least 1920
        if not int(item[1]) >= 1920:
            return 0 
        # at most 2002
        if not int(item[1]) <= 2002:
            return 0 
        return 1

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif item[0] == "iyr":
        # four digits
        if not len(item[1]) == 4:
            return 0
        #at least 2010
        if not int(item[1]) >= 2010:
            return 0 
        # at most 2020
        if not int(item[1]) <= 2020:
            return 0 
        return 1

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif item[0] == "eyr":
        # four digits
        if not len(item[1]) == 4:
            return 0
        #at least 2010
        if not int(item[1]) >= 2020:
            return 0 
        # at most 2020
        if not int(item[1]) <= 2030:
            return 0 
        return 1
        
    # hgt (Height) - a number followed by either cm or in:
    elif item[0] == "hgt":
        # check if last 2 characters are a number -> invalid
        if item[1][-2:].isnumeric():
            return 0

        # If cm, the number must be at least 150 and at most 193.
        if "cm" == item[1][-2:]:
            if not int(item[1][:-2]) >= 150:
                return 0
            
            if not int(item[1][:-2]) <= 193:
                return 0

        # If in, the number must be at least 59 and at most 76.
        elif "in" == item[1][-2:]:
            if not int(item[1][:-2]) >= 59:
                return 0
            
            if not int(item[1][:-2]) <= 76:
                return 0

        # anything else is invalid too
        else:
            return 0

        return 1

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif item[0] == "hcl":
        # check if first char is #
        if not item[1][0] == "#":
            return 0
        
        # check if the length is 1+6 characters
        if not len(item[1]) == 7:
            return 0
        
        # check if chars in voc
        voc = "0123456789abcdef"
        tar = list(item[1][1:])
        for i in tar:
            if i not in voc:
                return 0
        
        return 1

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif item[0] == "ecl":
        voc = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for v in voc:
            if item[1] == v:
                return 1 
                
        return 0
        

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif item[0] == "pid":
        if not item[1].isnumeric():
            return 0
        if not len(item[1]) == 9:
            return 0
        print(item)
        return 1

    # cid (Country ID) - ignored, missing or not.
    
    # when invalid
    return 0

with open("input.txt", "r") as file:
    line = file.read()
    line = line.replace(" ", ",")
    line = line.replace("\n\n", ";")
    line = line.replace("\n", ",")

    data = line.split(";")

    # keys must be on passport
    policy = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid"]

    passcounter = 0
    for item in data:
        parse = item.split(",")
        invalid = 0 
        valid = 0
        for entry in parse:
            # when an entry is valid: count them
            if entry.split(":")[0] in policy:
                #print("found valid entry: ",entry.split(":")[0])
                valid += validate(entry.split(":"))
            else:
                # edgecase from task cid
                if not entry.split(":")[0] == "cid":
                    invalid = 1
                    print("entry not valid: ", entry.split(":"))

        if not invalid and valid >=7:
            passcounter += 1
    
    print(passcounter)