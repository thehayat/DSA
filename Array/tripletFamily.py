"Question"
# https://practice.geeksforgeeks.org/problems/triplet-family/1/?ref=self
def findTriplet(arr,n):
    arr.sort()
    arr_set = set(arr)

    # count = 0
    output = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if i != j:
                if arr[i] + arr[j] in arr_set:
                    output.append((arr[i], arr[j], arr[i] + arr[j]))
                
                # if (arr[i] + arr[j]) > arr[-1]:
                #     break
                
                if len(output) >=3:
                    return output
                    # count += 1
    return output

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size= int(input())
        arr = list(map(int,input().strip().split()))
        print(findTriplet(arr))