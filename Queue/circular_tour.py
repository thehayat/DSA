"Question"
# https://practice.geeksforgeeks.org/problems/circular-tour/1

def tour(lis, n):
    differnce = [each[0] - each[1] for each in lis]
    i = 0
    count =0
    while i <= n:
        sum_ = 0
        count = 0
        for j in range(i,i+n):
            
            sum_ = sum_ + differnce[j%n]
            if sum_ >= 0:
                count = count+1

            else:
                i += 1
                break 
        if count == n:
            return i
    
    return -1
if __name__ == "__main__":

    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        #print n, arr
        print(tour(lis, n))

