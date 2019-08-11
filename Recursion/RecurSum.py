def recur_sum(arr):
    if len(arr) < 2:
         return arr[0]
    return recur_sum(arr[1:]) + arr[0]

if __name__ == "__main__":
    print(recur_sum([1,2,3]))