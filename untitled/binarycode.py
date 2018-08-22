

def encrypt(number):
    binaryCode = []
    exitValue = 0

    divValue = number
    j = 1
    while divValue != -1:
        modValue = divValue % 2
        binaryCode[j] = modValue
        j += 1
        if divValue == 0:
            divValue = -1
        else:
            divValue = divValue // 2
    for j in range(255):
        binaryCode[j] = 2

    for i in range(255, 1, -1):
        if binaryCode[i] != 2:
            exitValue += binaryCode[1]
    return exitValue


def decrypt(binaryCode):
    numbers = []
    binaryCode = 0
    exitValue = ""
    u = 1

    exitValue += binaryCode
    if exitValue[len(exitValue)] == '1':
        zeroOrOne = 1
    exitValue = exitValue[len(exitValue), 1]
    for i in exitValue:
        u *=2

    for i in range(2, len(exitValue, 1)):
        numbers[len(exitValue)] = exitValue[len(exitValue)]
        exitValue.replace(exitValue[len(exitValue)] + exitValue[5], "")
        e = 1


