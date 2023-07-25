def main():
    word = input()
    process(word)
    
def create_index_dict(data):
    index_dict = {}
    for row_idx, row in enumerate(data):
        for col_idx, element in enumerate(row):
            index_dict[element] = (row_idx, col_idx)
    return index_dict

def manhattan_distance(idx1, idx2):
    return abs(idx1[0] - idx2[0]) + abs(idx1[1] - idx2[1])

def process(word):
    data = [
        ['A', 'B', 'C', 'D', 'E', 'F'],
        ['G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z', ' ', '-', '.', 'Enter']
    ]
    dataDict = create_index_dict(data)
    # print(dataDict)
    res = manhattan_distance(dataDict["A"], dataDict[word[0]])
    for i in range(len(word)):
        pos1 = dataDict[word[i]]
        if i == len(word) - 1:
            pos2 = dataDict["Enter"]
        else:
            pos2 = dataDict[word[i+1]]
        res += manhattan_distance(pos1, pos2)
        # print(res, pos1, pos2)
    print(res)

main()