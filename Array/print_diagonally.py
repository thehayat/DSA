"Question"
# https://practice.geeksforgeeks.org/problems/print-diagonally/0

def diagonal(arr, n):
    arr = [-1]+arr
    output = []
    count = 2
    for i in range(n+1):
        
        idx = i
        for j in range(i):
            output.append(str(arr[idx]))
            idx += n - 1
    size_ = n
    
    for j in range(n-1):
        idx = n * count
        for k in range(size_-1):
            output.append(str(arr[idx]))
            idx += n - 1
        size_ = size_ - 1
        count +=1

    
        
    return " ".join(output)
            

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size = int(input())
        arr = list(map(int,input().strip().split()))
        print(diagonal(arr,size))
    
