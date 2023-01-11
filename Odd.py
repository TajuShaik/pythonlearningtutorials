n=int(input("enter a number:"))
print ("odd numbers upto given {} is". format (n))
sum=0
odd=range(1,n+1)
for i in odd:
    if i%2!=0:
       sum=i+sum
print("sum of odd numbers above is",sum)

