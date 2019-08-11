def permutation(string,step =0 ):
    if step == len(string):
        print("".join(string))
    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutation(string_copy, step + 1)
        
if __name__ == "__main__":
    permutation("abcd")