"Question"
# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0/?ref=self


def find_missing_number(arr, n):
    acutal_sum = int((n * (n + 1)) / 2)
    given_sum = int(sum(arr))
    return acutal_sum - given_sum

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(find_missing_number(arr,n))
    