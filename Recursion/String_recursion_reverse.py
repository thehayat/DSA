def ReverseString(string):
    if len(string) < 2:
      return string
    return ReverseString(string[1:]) + string[0]
if __name__ == "__main__":
    string = input()
    print(ReverseString(string))