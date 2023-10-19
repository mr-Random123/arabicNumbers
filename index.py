import json
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
        
def trailingZeros(ndigits, digits):
    #print(translate(digits[0], 1))
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
            finalOut = translate(newDigits[0], 3) + " wa " + translate(newDigits[1], 1) + " wa " + translate(newDigits[2], 2)
        case 2:
            finalOut = translate(newDigits[0], 1) + " wa " + translate(newDigits[1], 2)
    print(finalOut)

def moreThan3(ndigits:str):
    digits = list(ndigits)
    group = []
    newDigits = []
    print(ndigits == '1000' or ndigits == '2000' or ndigits == '3000' or ndigits == '4000' or ndigits == '5000' or ndigits == '6000' or ndigits == '7000' or ndigits == '8000' or ndigits == '9000')
    if ndigits == '1000' or ndigits == '2000' or ndigits == '3000' or ndigits == '4000' or ndigits == '5000' or ndigits == '6000' or ndigits == '7000' or ndigits == '8000' or ndigits == '9000':
        print(translate(digits[0], 4))
        return None
    for i, digit in enumerate(digits[::-1]):
        group.append(digit)
        print("i: "+str(i)+" digit: "+str(len(digits)-1)+" group: "+str(len(group)))
        print(len(group) == 3)
        print(i == len(digits)-1 and len(group) == 1)
        print(i == len(digits)-1 and len(group) == 2)
        if len(group) == 3:
            group[1], group[2] = group[2], group[1] 
            newDigits.append(group[::-1])
            group = []
        elif i == len(digits)-1 and len(group) == 1:
            newDigits.append(group)
            group = []
        elif i == len(digits)-1 and len(group) == 2:
            group[0], group[1] = group[1], group[0] 
            newDigits.append(group[::-1])
            group = []
    newDigits = newDigits[::-1]
    print(newDigits)
    print(len(newDigits))
    finalOut = ""
    match len(newDigits):
        case 2:
            if len(newDigits[0]) == 3:
                string1 = ""
                string2 = ""
                print(newDigits[0][1:] == ['0', '0'])
                print(newDigits[0][1:])
                if newDigits[0][1:] == ['0', '0']:
                    string1 = translate(1, 3) + " " + translate(1, 4, True)
                elif newDigits[0][1:] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0']:
                    string1 = translate(1, 2) + " " + translate(1, 4)

                if newDigits[1] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0', '0']:
                    string2 = translate(1, 3)
                elif newDigits[1][1:] == ['1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9', '0']:
                    string2 = translate(1, 2)  
                
                if string1 == None and string2 == None:
                    match len(newDigits[0]):
                        case 3:
                             string1 = finalOut = translate(newDigits[0][0], 3) + " wa " + translate(newDigits[0][1], 1) + " wa " + translate(newDigits[0][2], 2)
                        case 2:
                            string2 = finalOut = translate(newDigits[0][0], 1) + " wa " + translate(newDigits[0][1], 2)
                        case 1:
                            string2 = finalOut = translate(newDigits[0][0], 1)
                    match len(newDigits[1]):
                        case 3:
                            string2 = finalOut = translate(newDigits[1][0], 3) + " wa " + translate(newDigits[1][1], 1) + " wa " + translate(newDigits[1][2], 2)
                        case 2:
                            string2 = finalOut = translate(newDigits[1][0], 1) + " wa " + translate(newDigits[1][1], 2)
                        case 1:
                            string2 = finalOut = translate(newDigits[1][0], 1)
                if newDigits[1] != ['0', '0', '0']:
                    finalOut = string1 + " wa " + string2
                else:
                    finalOut = string1
            
    print(finalOut)
                


def main():
    global numbers
    numbers = json.load(open("arabicNumbers.json"))
    while True:
        i1 = input("add number:")
        if i1.isnumeric():
            digits = list(i1)
            if len(digits) > 3:
                moreThan3(str(int(i1)))
            else:
                lessThanOrEqual3(str(int(i1)))
        else:
            break
        
if __name__ == '__main__':
    main()