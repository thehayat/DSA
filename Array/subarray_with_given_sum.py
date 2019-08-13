"Question"
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0/?ref=self
def subarray(arr, s):
    if not sum(arr) >= s:
        return -1
    for i in range(len(arr)):
        sum_= 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if sum_ == s:
                return "{} {}".format(i + 1, j + 1)
            elif sum_ > s:
                break
    
    return -1
if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size, s = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(subarray(arr, s))
        
    