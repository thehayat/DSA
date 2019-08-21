"Question"
# https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array/0/?ref=self

def second_minimum(arr, size):
    maximum = arr[0]
    minimum = arr[0]
    for each in arr[1:]:
        if each > maximum:
           maximum = each
        if each < minimum:
            minimum = each
    print("{} {}".format(minimum,maximum))


if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        size = int(input())
        arr = list(map(int, input().strip().split()))
        second_minimum(arr,size)