"Question"
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0/?ref=self

def sort_array(arr,s):
    arr.sort()
    print(*arr,sep= " ")


if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size = int(input())
        arr = list(map(int,input().strip().split()))
        sort_array(arr, size)
        
    