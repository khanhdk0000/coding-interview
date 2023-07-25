def solution(S):
    # Implement your solution here
    files = S.split('\n')
    res = 0


    for file in files:
        columns = file.split()
        fileName = columns[-1]
        if fileName.endswith('~'):
            sizeStr = columns[0]
            size = 0
            if sizeStr[-1] == 'K':
                size = int(sizeStr[:-1]) * 2**10
            elif sizeStr[-1] == 'M':
                size = int(sizeStr[:-1]) * 2**20
            elif sizeStr[-1] == 'G':
                size = int(sizeStr[:-1]) * 2**30
            else:
                size = int(sizeStr)
           
            if size < 14 * (2**20):
                dateStr = columns[1]
                yearStr, monthStr, dayStr = dateStr.split("-")


                year = int(yearStr)
                month = int(monthStr)
                day = int(dayStr)


                if year > 1990 or (year == 1990 and month > 1):
                    lenFile = len(('.').join(fileName.split('.')[:-1]))
                    if res == 0:
                        res = lenFile
                    else:
                        res = min(lenFile, res)


    return str(res) if res > 0 else "NO FILES"


input = ' 715K 2009-09-23 system.zip~\n 179K 2013-08-14 totdasdas.xml~\n 645K 2013-06-19 blockbuster.mpeg~\n  536 2010-12-12 notes.html\n 688M 1990-02-11 delete-this.zip~\n  23K 1987-05-24 setup.png~\n 616M 1965-06-06 important.html\n  13M 2000-05-31 cruc.ialava~\n 192K 1990-01-31 very-long-filename.dll~'
print(solution(input))
fileName = "abcasdfsdfsa.pi.adasd"
print(('.').join(fileName.split('.')[:-1]))
