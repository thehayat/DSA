"Question"
# https://practice.geeksforgeeks.org/problems/element-appearing-once/0


def GetSingleOccured(arr):
    myDict = {}
    for  each in arr:
        if each not in myDict.keys():
            myDict[each]=1
        else:
            myDict.pop(each)
    return list(myDict.keys())[0]

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        n = int(input())
        arr = list(map(int,input().split()))

        print(GetSingleOccured(arr))