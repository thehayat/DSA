# https://practice.geeksforgeeks.org/problems/missing-element-of-ap/0/?ref=self
# S =(n/2)[2a + (n- 1)d] | S= N/2[a+l]

def findmissingAP(arr: list):
    sum_ = ((len(arr) + 1) * (arr[0] + arr[-1]))//2
    requiredNum =sum_ - sum(arr)
    return requiredNum

if __name__ == "__main__":
    testcase = int(input())
    for each in range(testcase):
        arrLen = int(input())
        arr = list(map(int, (input().split())))
        print(findmissingAP(arr))
