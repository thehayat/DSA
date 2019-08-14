"Question"
# https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not/1

def isIsogram(string):
    temp = []
    for each in string:
        if each not in temp:
            temp.extend(each)
        else:
            return False
    return True

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        string = input()
        print(isIsogram(string))
    
