import json
##############################################################################
##############################################################################
####### this is why comp has vb6 :sob:                           #############
##############################################################################
##############################################################################


def translate(number:str, place:int, Special = False) -> str:
    number = int(number)
    if Special:
        return numbers["1000S"]
    match place:
        case 1:
            return numbers[str(number)]
        case 2:
            return numbers[str(number*10)]
        case 3:
            return numbers[str(number*100)]
        case 4:
            return numbers[str(number*1000)]

def cleanUp(romanized:str) -> str:
    replacingWords = ["ahada ashar","ithna ashar","thalatha ashar","arba'a ashar","hhamsa ashar","sitta ashar","sab'a ashar","thamaniya ashar","tis'a ashar"]
    keyWords = ["wahid wa ashar","ithnan wa ashar","thalathah wa ashar","arba'a wa ashar","hhamsa wa ashar","sitta wa ashar","sab'a wa ashar","thamaniya wa ashar","tis'a wa ashar",]
    final = romanized
    for i, keyWord in enumerate(keyWords):
        final = final.replace(keyWord, replacingWords[i])
    return final
def trailingZeros(ndigits, digits):
    match int(ndigits):
        case 100| 200| 300| 400| 500| 600| 700| 800| 900:
            return translate(digits[0], 3)
        case 10| 20| 30| 40| 50| 60| 70| 80| 90:
            return translate(digits[0], 2)
        case 1| 2| 3| 4| 5| 6| 7| 8| 9:
            return translate(digits[0], 1)
        case _:
            return None
        
def lessThanOrEqual3(ndigits:str):
    digits = list(ndigits)
    group = []
    newDigits = []
    if trailingZeros(int(ndigits), digits) != None:
        print(trailingZeros(int(ndigits), digits))
        return None
    for i, digit in enumerate(digits):
        group.append(digit)
        if len(group) == 3:
            group[1], group[2] = group[2], group[1] 
            newDigits.extend(group)
            group = []
        elif i == len(digits)-1 and len(group) == 2:
            group[0], group[1] = group[1], group[0] 
            newDigits.extend(group)
            group = []
    finalOut = ""
    match len(newDigits):
        case 3:
            if newDigits[2] == '0':
                finalOut = translate(newDigits[0], 3) + " wa " + translate(newDigits[1], 1)
            else:
                finalOut = translate(newDigits[0], 3) + " wa " + translate(newDigits[1], 1) + " wa " + translate(newDigits[2], 2)
        case 2:
            finalOut = translate(newDigits[0], 1) + " wa " + translate(newDigits[1], 2)
    print(cleanUp(finalOut))

def moreThan3(ndigits:str):
    digits = list(ndigits)
    group = []
    newDigits = []
    match int(ndigits):
        case 1000| 2000| 3000| 4000| 5000| 6000| 7000| 8000| 9000:
            return None
    for i, digit in enumerate(digits[::-1]):
        group.append(digit)
        if len(group) == 3:
            group = group[::-1]
            group[1], group[2] = group[2], group[1] 
            newDigits.append(group)
            group = []
        elif i == len(digits)-1 and len(group) == 1:
            newDigits.append(group)
            group = []
        elif i == len(digits)-1 and len(group) == 2:
            group = group[::-1]
            group[0], group[1] = group[1], group[0] 
            newDigits.append(group)
            group = []
    newDigits = newDigits[::-1]
    finalOut = ""
    match len(newDigits):
        case 2:
            if len(newDigits[0]) == 3:
                string1 = ""
                string2 = ""
                if newDigits[0][1:] == ['0', '0']:
                    string1 = translate(1, 3) + " " + translate(1, 4, True)
                elif newDigits[0][1:] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0']:
                    string1 = translate(1, 2) + " " + translate(1, 4)

                if newDigits[1] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0', '0']:
                    string2 = translate(1, 3)
                elif newDigits[1][1:] == ['0', '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9']:
                    string2 = translate(1, 2)  
                if string1 == "" and string2 == "":
                    match len(newDigits[0]):
                        case 3:
                            if newDigits[0][2] == '0':
                                string1 = finalOut = translate(newDigits[0][0], 3) + " wa " + translate(newDigits[0][1], 1) + " " + translate(1, 4, True)
                            else:
                                string1 = finalOut = translate(newDigits[0][0], 3) + " wa " + translate(newDigits[0][1], 1) + " wa " + translate(newDigits[0][2], 2) + " " + translate(1, 4, True)
                        case 2:
                            string1 = finalOut = translate(newDigits[0][0], 1) + " wa " + translate(newDigits[0][1], 2) + " " + translate(1, 4, True)
                        case 1:
                            string1 = finalOut = translate(newDigits[0][0], 1)
                    match len(newDigits[1]):
                        case 3:
                            print(newDigits[1][2])
                            if newDigits[1][2] == '0':
                                string2 = finalOut = translate(newDigits[1][0], 3) + " wa " + translate(newDigits[1][1], 1)
                            else:
                                string2 = finalOut = translate(newDigits[1][0], 3) + " wa " + translate(newDigits[1][1], 1) + " wa " + translate(newDigits[1][2], 2)
                        case 2:
                            string2 = finalOut = translate(newDigits[1][0], 1) + " wa " + translate(newDigits[1][1], 2)
                        case 1:
                            string2 = finalOut = translate(newDigits[1][0], 1)
                if newDigits[1] != ['0', '0', '0']:
                    finalOut = string1 + " wa " + string2
                else:
                    finalOut = string1
            elif len(newDigits[0]) <= 2:
                string1 = ""
                string2 = ""
                if newDigits[0][1:] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0']:
                    string1 = translate(1, 2) + " " + translate(1, 4)
                if newDigits[1] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0', '0']:
                    string2 = translate(1, 3)
                elif newDigits[1][1:] == ['0', '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9']:
                    string2 = translate(1, 2)  
                
                if string1 == "" and string2 == "":
                    match len(newDigits[0]):
                        case 2:
                            string1 = finalOut = translate(newDigits[0][0], 1) + " wa " + translate(newDigits[0][1], 2) + " " + translate(1, 4, True)
                        case 1:
                            string1 = finalOut = translate(newDigits[0][0], 4)
                    match len(newDigits[1]):
                        case 3:
                            if newDigits[1][2] == '0':
                                string2 = finalOut = translate(newDigits[1][0], 3) + " wa " + translate(newDigits[1][1], 1)
                            else:
                                string2 = finalOut = translate(newDigits[1][0], 3) + " wa " + translate(newDigits[1][1], 1) + " wa " + translate(newDigits[1][2], 2)
                        case 2:
                            string2 = finalOut = translate(newDigits[1][0], 1) + " wa " + translate(newDigits[1][1], 2)
                        case 1:
                            string2 = finalOut = translate(newDigits[1][0], 1)
                if newDigits[1] != ['0', '0', '0']:
                    finalOut = string1 + " wa " + string2
                else:
                    finalOut = string1
    print(cleanUp(finalOut))
                
def main():
    global numbers
    numbers = json.load(open("arabicNumbers.json"))
    while True:
        i1 = input("add number:")
        if i1.isnumeric():
            digits = list(i1)
            if len(digits) >= 7:
                print("too big of a number")
            elif len(digits) > 3:
                moreThan3(str(int(i1)))
            else:
                lessThanOrEqual3(str(int(i1)))
        else:
            break
        
if __name__ == '__main__':
    main()