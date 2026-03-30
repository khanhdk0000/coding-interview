class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1OddDict, s2OddDict = {}, {}
        s1EvenDict, s2EvenDict = {}, {}
        for i in range(len(s1)):
            if i % 2 == 0:
                s1EvenDict[s1[i]] = s1EvenDict.get(s1[i], 0) + 1
                s2EvenDict[s2[i]] = s2EvenDict.get(s2[i], 0) + 1
            else:
                s1OddDict[s1[i]] = s1OddDict.get(s1[i], 0) + 1
                s2OddDict[s2[i]] = s2OddDict.get(s2[i], 0) + 1
        s2OddDictSorted = {k: s2OddDict[k] for k in s1OddDict if k in s2OddDict}
        s2EvenDictSorted = {k: s2EvenDict[k] for k in s1EvenDict if k in s2EvenDict}
        return s1OddDict == s2OddDictSorted and s1EvenDict == s2EvenDictSorted