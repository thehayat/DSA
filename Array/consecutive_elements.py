"Question"
# https://practice.geeksforgeeks.org/problems/consecutive-elements/0

def consecutive_element(string):
    result = string[0]
    count = 0
    for each in string[1::]:
        if each!=result[count]:
            result+=each
            count += 1
    return result
if __name__=="__main__":
    testCase = int(input())
    for i in range(testCase):
        string = input()
        print(consecutive_element(string))