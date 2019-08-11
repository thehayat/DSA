"Question"
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0def
def rotate_array(arr,k):
    output = arr[k:]+arr[:k:]
    print(*output,sep=" ")



if __name__=="__main__":
    testcase = int(input())
    for i in range(testcase):
        inpt = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        rotate_array(arr,inpt[1])