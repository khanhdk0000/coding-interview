import re
def main():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input())

    process(files)

def process(files):
    last = {}
    for name in files:
        modified = name
        if name in last:
            k = last[name]
            while modified in last:
                k += 1
                modified = f'{name}({k})'
            last[name] = k
        last[modified] = 0
    for k in last.keys():
        print(k)
    # return last.keys()
# main()
input = ["gta","gta(1)","gta","avalon"]
process(input)