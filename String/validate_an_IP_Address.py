def isValid(string):
    ipval = string.split(".")
    flag = 1
    if len(ipval) == 4:
        for each in ipval:
            if (len(each)>=2 and (int(each[1]) <= 0 and int(each[0]) <= 0)) or (int(each) > 256) or (int(each) < 0):
                flag = 0
    else:
        flag = 0

    return flag
if __name__ == '__main__':
    testCase = int(input())
    for i in range(testCase):
        string = input()
    print(isValid(string))


