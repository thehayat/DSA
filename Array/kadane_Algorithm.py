"Question"
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

def maxSubarray(arr, size):
    # if sum(arr) < 0:
    #     return max(arr)
    max_so_far = 0
    current_max_sum = 0
    # max_ending_here = 0
    for i in range(len(arr)):
        current_max_sum += arr[i]
        # print(current_max_sum)
    
        if current_max_sum > max_so_far:
            max_so_far = current_max_sum
        if current_max_sum < 0:
            current_max_sum = 0
        
    return max(arr) if max_so_far ==0 else max_so_far


    
if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size = int(input())
        arr = list(map(int,input().strip().split()))
        print(maxSubarray(arr,size))
    