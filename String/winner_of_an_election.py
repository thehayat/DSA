"Question"
# https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names/1/?ref=self

def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=input().strip().split()
        
        winner(arr,n)
        print()
        
        T -= 1
        
def winner(arr,n):
    #Your code here
     
    name_dict = {}
    for name in arr:
        if name in name_dict.keys():
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    
    maxium = max(name_dict.values())
    if len(set(name_dict.values())) == len(arr):
        name = sorted(name_dict)[0]
    else:
        
        name = sorted([k for k, v in name_dict.items() if int(v) == int(maxium)])[0]
    print("{}{}".format(name,maxium),end=" ")

if __name__=="__main__":
    main()
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
#Complete this function
