"""
Solving a to the b through recursion. 
"""
def Recur_power(a, b):
    if b == 0:
        return 1
    temp = Recur_power(a, int(b / 2))
    if b % 2 == 0:
        return temp*temp

    else:
        if b > 0:
            return a * temp * temp
        else:
            return (temp*temp)/a

if __name__ == "__main__":
    print(Recur_power(2,-4))
