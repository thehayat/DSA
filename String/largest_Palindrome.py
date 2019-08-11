"Question"
# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0

def largest_palindrome(string):
    maxpalindrome = {"size": 1, "value": string[0]}
    if string == string[::-1]:
        result = string
        return result
    else:
        for i, each in enumerate(string[1:]):
            for j in range(0, len(string)):
                temp = string[i: len(string) - j:]
                if temp == temp[::-1]:
                    if len(temp) > maxpalindrome['size']:
                        maxpalindrome['size'] = len(temp)
                        maxpalindrome['value'] = temp
    return maxpalindrome['value']


if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        string = str(input())
        print(largest_palindrome(string))
