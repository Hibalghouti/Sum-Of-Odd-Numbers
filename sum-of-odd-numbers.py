n=int(input("Enter an Integer:"))
sum=0

for i in range(1,n+1,2):
    sum=sum+i

print("the sum of odd numbers up to",n,"is",sum)