"Question"
# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/1/?ref=self

def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T -= 1
def subArrayExists(arr,n):
    ##Your code here
    if 0 in arr:
        return True
    else:
        for i in range(len(arr)):
            sum_ = 0
            for j in range(i, len(arr)):
                sum_ += arr[j]
                if -sum_ ==0:
                    return True
        else:
            return False

if __name__=="__main__":
    main()
