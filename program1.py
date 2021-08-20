n=int(input("terms:"))
x=int(input("x:"))
sum=x;fact=1
for i in range(2,n+1):
    fact*=i
    sum+=(-x)**i/fact
print("the sum of series is",round(sum,1))