"Question"
# https://practice.geeksforgeeks.org/problems/count-the-triplets/0/?ref=self


def countTriples(arr):
    arr.sort
    arr_set = tuple(arr)
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if i != j:
                if arr[i] + arr[j] in arr_set:
                    count += 1
                

    return -1 if count==0 else count

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size= int(input())
        arr = list(map(int,input().strip().split()))
        print(countTriples(arr))
        