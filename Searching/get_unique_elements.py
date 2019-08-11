"Question"
# https://practice.geeksforgeeks.org/problems/element-appearing-once/0

def GetSingleOccured(arr:list):
    myDict = {}
    for  each in arr:
        if each not in myDict.keys():
            myDict[each]=1
        else:
            myDict.pop(each)
    return list(myDict.keys())[0]

def GetSingleOccurence(arr:list):
    idx = 0
    while len(arr) > 1:
        if arr[0] in arr[idx+1:]:
            arr.remove(idx)
            arr.pop(arr.index(arr[0]))
        else:
            break
    return arr[0]

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        n = int(input())
        arr = list(map(int,input().split()))

        print(GetSingleOccurence(arr))