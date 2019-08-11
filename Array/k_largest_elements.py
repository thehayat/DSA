"Question"
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0
def k_largest_elements_(arr, n):
    arr.sort(reverse=True)
    return arr[:n]

if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        lenth, n = list(map(int, input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(*k_largest_elements_(arr,n),sep=" ")
