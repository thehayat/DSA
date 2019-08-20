"Question"
# https://practice.geeksforgeeks.org/problems/maximum-index/0/?ref=self

"34 8 10 3 2 80 30 33 1"

def maximun_Index(l,n):
    
    max_=0
    i = 0
    while(i<n):
        j=n-1
        while(j>i):
            if(l[i]<=l[j]):
                if(j-i>max_):
                    max_=j-i
                break
            j-=1
        i+=1
    print(max_)
                
                

        

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size = int(input())
        arr = list(map(int,input().strip().split()))
        maximun_Index(arr,size)
    