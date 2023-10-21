import json
global numbers
numbers = json.load(open("arabicNumbers.json"))

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
    keyWords = ["wahid wa ashar","ithnan wa ashar","thalathah wa ashar","arba'a wa ashar","hhamsa wa ashar","sitta wa ashar","sab'a wa ashar","thamaniya wa ashar","tis'a wa ashar"]
    final = romanized
    for i, keyWord in enumerate(keyWords):
        final = final.replace(keyWord, replacingWords[i])
    return final

def trailingZeros(ndigits):
    match int(ndigits):
        case 1000| 2000| 3000| 4000| 5000| 6000| 7000| 8000| 9000:
            return translate(ndigits[0], 4)
        case 100| 200| 300| 400| 500| 600| 700| 800| 900:
            return translate(ndigits[0], 3)
        case 10| 20| 30| 40| 50| 60| 70| 80| 90:
            return translate(ndigits[0], 2)
        case 1| 2| 3| 4| 5| 6| 7| 8| 9:
            return translate(ndigits[0], 1)
        case _:
            return None
        
def lessThanOrEqual3(ndigits:str):
    finalOut = ""
    if trailingZeros(ndigits) != None:
        return trailingZeros(ndigits)
    
    match len(ndigits):
        case 3:
            if ndigits[1] == '0':
                finalOut = translate(ndigits[0], 3) + " wa " + translate(ndigits[2], 1)
            elif ndigits[2] == '0':
                finalOut = translate(ndigits[0], 3) + " wa " + translate(ndigits[1], 2)
            else:
                finalOut = translate(ndigits[0], 3) + " wa " + translate(ndigits[2], 1) + " wa " + translate(ndigits[1], 2)
        case 2:
            finalOut = translate(ndigits[1], 1) + " wa " + translate(ndigits[0], 2)
    return cleanUp(finalOut)

def moreThan3(ndigits:str):
    if trailingZeros(ndigits) != None:
        return trailingZeros(ndigits)
    
    newDigits = []
    group = []
    for i, digit in enumerate(ndigits[::-1]):
        group.append(digit)
        if len(group) == 3:
            newDigits.append(group[::-1])
            group = []
        elif i == len(ndigits)-1 and len(group) < 3:
            newDigits.append(group[::-1])
            group = []
    newDigits = newDigits[::-1]
    string = lessThanOrEqual3(''.join(newDigits[0])) +" "+ translate(1, 4, True) +" wa "+lessThanOrEqual3(''.join(newDigits[1]))
    return string
    
def main():
    finalOut = ""
    while True:
        i1 = input("add number:")
        if not i1.isnumeric():
            break

        if len(i1) >= 7:
            print("too big of a number")
        elif len(i1) > 3:
            finalOut = moreThan3(i1)
        else:
            finalOut = lessThanOrEqual3(i1)
        print(finalOut)
    input("exiting... press any key to continue")
if __name__ == '__main__':
    main()