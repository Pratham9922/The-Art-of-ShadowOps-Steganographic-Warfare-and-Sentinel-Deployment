def gcd_on(a,b):
    #Time Complexity -> O(min(a,b))
    min_ab = min(a, b)
    gcd = 1
    for i in range(1, min_ab + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_euclidean(a,b):

    #Time Complexity -> O(log)
    while b:
        temp=a%b
        a=b
        b=temp
    return a


a=int(input("Enter the first integer(a): "))
b=int(input("Enter the second integer(b): "))

gcd_on_ans=gcd_on(a,b)
gcd_euclidean_ans=gcd_euclidean(a,b)

print("gcd_on answer is : ",gcd_on_ans(a,b))
print("gcd_euclidean ans is: ",gcd_euclidean_ans)
    
