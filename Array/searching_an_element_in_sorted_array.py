"Question"
# https://practice.geeksforgeeks.org/problems/who-will-win/0
def findElement(arr,element):
    return 1 if element in arr else -1

if __name__=="__main__":
    testcase= int(input())
    for i in range(testcase):
        temp = input().strip().split()
        arr = list(map(int,input().strip().split()))
        print(findElement(arr,int(temp[1])))