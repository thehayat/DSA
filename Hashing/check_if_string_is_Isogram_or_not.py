"Question"
# https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not/1

def isIsogram(string):
    
    return True if len(set(string))==len(string) else False

if __name__ == '__main__':
    testcase = int(input())
    for i in range(testcase):
        string = input()
        print(isIsogram(string))
    
