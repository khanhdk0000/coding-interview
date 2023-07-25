def converRight(s):
    if s == "read":
        return "R"
    elif s == "write":
        return "W"
    else:
        return "X"

def main():
    fileMap = {}
    numberOfFiles = input()
    for i in range(int(numberOfFiles)):
        line = input()
        lineSplit = line.split(" ")
        fileName = lineSplit[0]
        fileMap[fileName] = lineSplit[1:]

    numCommand = input()
    for _ in range(int(numCommand)):
        line = input()
        lineSplit = line.split(" ")
        command, file = lineSplit[0], lineSplit[1]
        if (converRight(command) not in fileMap[file]):
            print("Access denied")
        else:
            print("OK")