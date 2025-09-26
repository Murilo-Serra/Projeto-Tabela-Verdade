while True:
    language_select = int(input("1 - Português | 2 - English"))
    if language_select > 2:
        pass
    elif language_select < 1:
        pass
    else:
        break

while True:
    if language_select == 1:
        qntProp = int(input("Insira a quantidade de proposicões que serão utilizadas (max 5, min 2): "))
        if 6 > qntProp > 1:
            break
        else:
            print("Input invalido.")
    if language_select == 2:
        qntProp = int(input("Insert the quantities of logical variables to be used. (max 5, min 2): "))
        if 6 > qntProp > 1:
            break
        else:
            print("Invalid input.")
while True:
    userInput = str(input("\nInsira uma fórmula contendo a quantidade de proposições selecionadas. \n(para uma lista de comandos, digite /help.) Input: "))
    if userInput == "/help":
        print("Comandos: \nand / e = x AND y \nor / ou = x OR y \nxor / ou exclusivo = x XOR y \nse e somente se / sss = x <-> y \nse / então = x -> y \nnand / not and = x NAND y \nnor / not or = x NOR y \nnot / não = nx (ex: x AND ny)")
    else:
        break

endPrint = userInput
userInput = userInput.lower()

userInput = userInput.replace(" nor ", "!")
userInput = userInput.replace(" nor", "!")
userInput = userInput.replace("nor ", "!")
userInput = userInput.replace("nor", "!")

userInput = userInput.replace(" nand ", "$")
userInput = userInput.replace(" nand", "$")
userInput = userInput.replace("nand ", "$")
userInput = userInput.replace("nand", "$")

userInput = userInput.replace(" and ", "&")
userInput = userInput.replace("and ", "&")
userInput = userInput.replace(" and", "&")
userInput = userInput.replace("and", "&")

userInput = userInput.replace(" xor ", "Y")
userInput = userInput.replace("xor ", "Y")
userInput = userInput.replace(" xor", "Y")
userInput = userInput.replace("xor", "Y")

userInput = userInput.replace(" or ", "U")
userInput = userInput.replace("or ", "U")
userInput = userInput.replace(" or", "U")
userInput = userInput.replace("or", "U")

userInput = userInput.replace(" <-> ", "<")
userInput = userInput.replace("<-> ", "<")
userInput = userInput.replace(" <->", "<")
userInput = userInput.replace("<->", "<")

userInput = userInput.replace(" -> ", ">")
userInput = userInput.replace("-> ", ">")
userInput = userInput.replace(" ->", ">")
userInput = userInput.replace("->", ">")

userInput = userInput.replace("np", "a")
userInput = userInput.replace("nq", "b")
userInput = userInput.replace("nr", "c")
userInput = userInput.replace("ns", "d")
userInput = userInput.replace("nt", "e")

userInputList = []

for i in range(len(userInput)):
    userInputList.append(userInput[i:i+1])

if qntProp == 2:
    p = ["V", "V", "F", "F"]
    q = ["V", "F", "V", "F"]
    a = ["F", "F", "V", "V"]
    b = ["F", "V", "F", "V"]

    for i in range(len(userInputList)):
        if userInputList[i] == "a":
            userInputList[i] = a

        elif userInputList[i] == "p":
            userInputList[i] = p

        elif userInputList[i] == "b":
            userInputList[i] = b

        elif userInputList[i] == "q":
            userInputList[i] = q

        else:
            continue

elif qntProp == 3:
    p = ["V", "V", "V", "V", "F", "F", "F", "F"]
    q = ["V", "V", "F", "F", "V", "V", "F", "F"]
    r = ["V", "F", "V", "F", "V", "F", "V", "F"]
    a = ["F", "F", "F", "F", "V", "V", "V", "V"]
    b = ["F", "F", "V", "V", "F", "F", "V", "V"]
    c = ["F", "V", "F", "V", "F", "V", "F", "V"]

    for i in range(len(userInputList)):
        if userInputList[i] == "a":
            userInputList[i] = a

        elif userInputList[i] == "p":
            userInputList[i] = p

        elif userInputList[i] == "b":
            userInputList[i] = b

        elif userInputList[i] == "q":
            userInputList[i] = q

        elif userInputList[i] == "c":
            userInputList[i] = c

        elif userInputList[i] == "r":
            userInputList[i] = r

        else:
            continue

elif qntProp == 4:
    p = ["V", "V", "V", "V", "V", "V", "V", "V", "F", "F", "F", "F", "F", "F", "F", "F"]
    q = ["V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F"]
    r = ["V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F"]
    s = ["V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F"]
    a = ["F", "F", "F", "F", "F", "F", "F", "F", "V", "V", "V", "V", "V", "V", "V", "V"]
    b = ["F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V"]
    c = ["F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V"]
    d = ["F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V"]

    for i in range(len(userInputList)):
        if userInputList[i] == "a":
            userInputList[i] = a

        elif userInputList[i] == "p":
            userInputList[i] = p

        elif userInputList[i] == "b":
            userInputList[i] = b

        elif userInputList[i] == "q":
            userInputList[i] = q

        elif userInputList[i] == "c":
            userInputList[i] = c

        elif userInputList[i] == "r":
            userInputList[i] = r

        elif userInputList[i] == "d":
            userInputList[i] = d

        elif userInputList[i] == "s":
            userInputList[i] = s

        else:
            continue

elif qntProp == 5:
    p = ["V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"]
    q = ["V", "V", "V", "V", "V", "V", "V", "V", "F", "F", "F", "F", "F", "F", "F", "F", "V", "V", "V", "V", "V", "V", "V", "V", "F", "F", "F", "F", "F", "F", "F", "F"]
    r = ["V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F"]
    s = ["V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F"]
    t = ["V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F"]
    a = ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V"]
    b = ["F", "F", "F", "F", "F", "F", "F", "F", "V", "V", "V", "V", "V", "V", "V", "V", "F", "F", "F", "F", "F", "F", "F", "F", "V", "V", "V", "V", "V", "V", "V", "V"]
    c = ["F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V", "F", "F", "F", "F", "V", "V", "V", "V"]
    d = ["F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V", "F", "F", "V", "V"]
    e = ["F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V", "F", "V"]

    for i in range(len(userInputList)):
        if userInputList[i] == "a":
            userInputList[i] = a

        elif userInputList[i] == "p":
            userInputList[i] = p

        elif userInputList[i] == "b":
            userInputList[i] = b

        elif userInputList[i] == "q":
            userInputList[i] = q

        elif userInputList[i] == "c":
            userInputList[i] = c

        elif userInputList[i] == "r":
            userInputList[i] = r

        elif userInputList[i] == "d":
            userInputList[i] = d

        elif userInputList[i] == "s":
            userInputList[i] = s

        elif userInputList[i] == "e":
            userInputList[i] = e

        elif userInputList[i] == "t":
            userInputList[i] = t
        else:
            continue


def xandy(x: list, y: list):
    tempand = x + y
    resultand = []
    for i in range((2 ** qntProp)):
        if tempand[i] == "V":
            if tempand[(2 ** qntProp) + i] == "F":
                resultand.append("F")
            else:
                resultand.append("V")
        else:
            resultand.append("F")
    return resultand


def xory(x: list, y: list):
    tempor = x + y
    resultor = []
    for i in range((2 ** qntProp)):
        if tempor[i] == "F":
            if tempor[(2 ** qntProp) + i] == "F":
                resultor.append("F")
            else:
                resultor.append("V")
        else:
            resultor.append("V")
    return resultor


def xxory(x: list, y: list):
    tempxor = x + y
    resultxor = []
    for i in range((2 ** qntProp)):
        if tempxor[i] == "F":
            if tempxor[(2 ** qntProp) + i] == "F":
                resultxor.append("F")
            else:
                resultxor.append("V")
        else:
            if tempxor[(2 ** qntProp) + i] == "V":
                resultxor.append("F")
            else:
                resultxor.append("V")
    return resultxor


def xsssy(x: list, y: list):
    tempsss = x + y
    resultsss = []
    for i in range((2 ** qntProp)):
        if tempsss[i] == "F":
            if tempsss[(2 ** qntProp) + i] == "F":
                resultsss.append("V")
            else:
                resultsss.append("F")
        else:
            if tempsss[(2 ** qntProp) + i] == "V":
                resultsss.append("V")
            else:
                resultsss.append("F")
    return resultsss


def xentaoy(x: list, y: list):
    tempentao = x + y
    resultentao = []
    for i in range((2 ** qntProp)):
        if tempentao[i] == "F":
            if tempentao[(2 ** qntProp) + i] == "F":
                resultentao.append("V")
            else:
                resultentao.append("V")
        else:
            if tempentao[(2 ** qntProp) + i] == "V":
                resultentao.append("V")
            else:
                resultentao.append("F")
    return resultentao


def xnandy(x: list, y: list):
    tempnand = x + y
    resultnand = []
    for i in range((2 ** qntProp)):
        if tempnand[i] == "F":
            if tempnand[(2 ** qntProp) + i] == "F":
                resultnand.append("V")
            else:
                resultnand.append("V")
        else:
            if tempnand[(2 ** qntProp) + i] == "V":
                resultnand.append("F")
            else:
                resultnand.append("V")
    return resultnand


def xnory(x: list, y: list):
    tempnor = x + y
    resultnor = []
    for i in range((2 ** qntProp)):
        if tempnor[i] == "F":
            if tempnor[(2 ** qntProp) + i] == "F":
                resultnor.append("V")
            else:
                resultnor.append("F")
        else:
            if tempnor[(2 ** qntProp) + i] == "V":
                resultnor.append("F")
            else:
                resultnor.append("F")
    return resultnor


def notx(x):
    resultnot = []
    for i in range(len(x)):
        if x[i] == "F":
            resultnot.append("V")
        else:
            resultnot.append("F")
    return resultnot


while "(" or ")" in userInputList:

    parentList = []
    try:
        marcador2 = userInputList.index(")")
    except:
        break
    marcador2 += 1

    for i in reversed(range(len(userInputList))):
        if userInputList[i] == "(":
            marcador0 = i
            marcador1 = i
            if marcador1 > marcador2:
                for i in range(len(userInputList)):
                    if userInputList[i] == "(":
                        marcador0 = i
                        marcador1 = i
                        break
            else:
                break
        else:
            continue
    if userInputList[marcador1-1] == "n":
        marcador0 -= 1
        marcador1 -= 1
        while marcador1 < marcador2:
            parentList.append(userInputList[marcador1])
            marcador1 +=1
    else:
        while marcador1 < marcador2:
            parentList.append(userInputList[marcador1])
            marcador1 +=1

    while "$" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "$":
                try:
                    parentList[i] = xnandy(parentList[i - 1], parentList[i + 1])
                    parentList[i - 1] = ""
                    parentList[i + 1] = ""
                except:
                    continue

            elif userInputList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while "&" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "&":
                try:
                    parentList[i] = xandy(parentList[i-1], parentList[i+1])
                    parentList[i-1] = ""
                    parentList[i+1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while "!" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "!":
                try:
                    parentList[i] = xnory(parentList[i - 1], parentList[i + 1])
                    parentList[i - 1] = ""
                    parentList[i + 1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while "U" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "U":
                try:
                    parentList[i] = xory(parentList[i-1], parentList[i+1])
                    parentList[i-1] = ""
                    parentList[i+1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while ">" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == ">":
                try:
                    parentList[i] = xentaoy(parentList[i-1], parentList[i+1])
                    parentList[i-1] = ""
                    parentList[i+1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while "<" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "<":
                try:
                    parentList[i] = xsssy(parentList[i-1], parentList[i+1])
                    parentList[i-1] = ""
                    parentList[i+1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp

    while "Y" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "Y":
                try:
                    parentList[i] = xxory(parentList[i-1], parentList[i+1])
                    parentList[i-1] = ""
                    parentList[i+1] = ""
                except:
                    continue

            elif parentList[i] == "(" and parentList[i + 2] == ")":
                parentList[i] = ""
                parentList[i + 2] = ""

            else:
                continue

        userInputTemp = []

        for i in range(len(parentList)):
            if parentList[i] != "":
                userInputTemp.append(parentList[i])
            else:
                continue

        parentList = userInputTemp


    userInputTemp = []

    for i in range(len(parentList)):
        if parentList[i] != "":
            userInputTemp.append(parentList[i])
        else:
            continue

    parentList = userInputTemp

    for i in range(len(parentList)):
        if parentList[i] == "(" and parentList[i + 2] == ")":
            parentList[i] = ""
            parentList[i + 2] = ""

    userInputTemp = []

    for i in range(len(parentList)):
        if parentList[i] != "":
            userInputTemp.append(parentList[i])
        else:
            continue

    parentList = userInputTemp

    while "n" in parentList:
        for i in range(len(parentList)):
            if parentList[i] == "n":
                parentList[i] = notx(parentList[i + 1])
                parentList[i + 1] = ""
        else:
            continue

    userInputTemp = []

    for i in range(len(parentList)):
        if parentList[i] != "":
            userInputTemp.append(parentList[i])
        else:
            continue

    parentList = userInputTemp

    parentList = parentList[0]

    for i in range(marcador2 - marcador0):
        if i + 1 < (marcador2 - marcador0):
            userInputList.pop(marcador0)
        else:
            userInputList[marcador0] = parentList

while "n" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "n":
            userInputList[i] = notx(userInputList[i+1])
            userInputList[i + 1] = ""

while "$" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "$":
            try:
                userInputList[i] = xnandy(userInputList[i - 1], userInputList[i + 1])
                userInputList[i - 1] = ""
                userInputList[i + 1] = ""
            except:
                continue

        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while "&" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "&":
            try:
                userInputList[i] = xandy(userInputList[i-1], userInputList[i+1])
                userInputList[i-1] = ""
                userInputList[i+1] = ""
            except:
                continue
        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while "!" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "!":
            try:
                userInputList[i] = xnory(userInputList[i - 1], userInputList[i + 1])
                userInputList[i - 1] = ""
                userInputList[i + 1] = ""
            except:
                continue
        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while "U" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "U":
            try:
                userInputList[i] = xory(userInputList[i-1], userInputList[i+1])
                userInputList[i-1] = ""
                userInputList[i+1] = ""
            except:
                continue

        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while ">" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == ">":
            try:
                userInputList[i] = xentaoy(userInputList[i-1], userInputList[i+1])
                userInputList[i-1] = ""
                userInputList[i+1] = ""
            except:
                continue

        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while "<" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "<":
            try:
                userInputList[i] = xsssy(userInputList[i-1], userInputList[i+1])
                userInputList[i-1] = ""
                userInputList[i+1] = ""
            except:
                continue

        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp

while "Y" in userInputList:
    for i in range(len(userInputList)):
        if userInputList[i] == "Y":
            try:
                userInputList[i] = xxory(userInputList[i-1], userInputList[i+1])
                userInputList[i-1] = ""
                userInputList[i+1] = ""
            except:
                continue
        else:
            continue

    userInputTemp = []

    for i in range(len(userInputList)):
        if userInputList[i] != "":
            userInputTemp.append(userInputList[i])
        else:
            continue

    userInputList = userInputTemp


result = userInputList[0]

if qntProp == 2:
    print(f"| p | q | {endPrint} |"
          f"\n| V | V | {result[0]} |"
          f"\n| V | F | {result[1]} |"
          f"\n| F | V | {result[2]} |"
          f"\n| F | F | {result[3]} |")

if qntProp == 3:
    print(f"| p | q | r | {endPrint} |"
          f"\n| V | V | V | {result[0]} |"
          f"\n| V | V | F | {result[1]} |"
          f"\n| V | F | V | {result[2]} |"
          f"\n| V | F | F | {result[3]} |"
          f"\n| F | V | V | {result[4]} |"
          f"\n| F | V | F | {result[5]} |"
          f"\n| F | F | V | {result[6]} |"
          f"\n| F | F | F | {result[7]} |")

if qntProp == 4:
    print(f"| p | q | r | s | {endPrint} |"
          f"\n| V | V | V | V |{result[0]} |"
          f"\n| V | V | V | F | {result[1]} |"
          f"\n| V | V | F | V | {result[2]} |"
          f"\n| V | V | F | F | {result[3]} |"
          f"\n| V | F | V | V | {result[4]} |"
          f"\n| V | F | V | F | {result[5]} |"
          f"\n| V | F | F | V | {result[6]} |"
          f"\n| V | F | F | F | {result[7]} |"
          f"\n| F | V | V | V | {result[8]} |"
          f"\n| F | V | V | F | {result[9]} |"
          f"\n| F | V | F | V | {result[10]} |"
          f"\n| F | V | F | F | {result[11]} |"
          f"\n| F | F | V | V | {result[12]} |"
          f"\n| F | F | V | F | {result[13]} |"
          f"\n| F | F | F | V | {result[14]} |"
          f"\n| F | F | F | F | {result[15]} |")

if qntProp == 5:
    print(f"| p | q | r | s | {endPrint} |"
          f"\n| V | V | V | V | V | {result[0]} |"
          f"\n| V | V | V | V | F | {result[1]} |"
          f"\n| V | V | V | F | V | {result[2]} |"
          f"\n| V | V | V | F | F | {result[3]} |"
          f"\n| V | V | F | V | V | {result[4]} |"
          f"\n| V | V | F | V | F | {result[5]} |"
          f"\n| V | V | F | F | V | {result[6]} |"
          f"\n| V | V | F | F | F | {result[7]} |"
          f"\n| V | F | V | V | V | {result[8]} |"
          f"\n| V | F | V | V | F | {result[9]} |"
          f"\n| V | F | V | F | V | {result[10]} |"
          f"\n| V | F | V | F | F | {result[11]} |"
          f"\n| V | F | F | V | V | {result[12]} |"
          f"\n| V | F | F | V | F | {result[13]} |"
          f"\n| V | F | F | F | V | {result[14]} |"
          f"\n| V | F | F | F | F | {result[15]} |"
          f"\n| F | V | V | V | V | {result[16]} |"
          f"\n| F | V | V | V | F | {result[17]} |"
          f"\n| F | V | V | F | V | {result[18]} |"
          f"\n| F | V | V | F | F | {result[19]} |"
          f"\n| F | V | F | V | V | {result[20]} |"
          f"\n| F | V | F | V | F | {result[21]} |"
          f"\n| F | V | F | F | V | {result[22]} |"
          f"\n| F | V | F | F | F | {result[23]} |"
          f"\n| F | F | V | V | V | {result[24]} |"
          f"\n| F | F | V | V | F | {result[25]} |"
          f"\n| F | F | V | F | V | {result[26]} |"
          f"\n| F | F | V | F | F | {result[27]} |"
          f"\n| F | F | F | V | V | {result[28]} |"
          f"\n| F | F | F | V | F | {result[29]} |"
          f"\n| F | F | F | F | V | {result[30]} |"
          f"\n| F | F | F | F | F | {result[31]} |")