#To get the factors of the given number upto the range of 10^8
import math
value=int(input())
divisors=list()
for i in range(1,int(math.sqrt(value))):
    if value%i==0:
        print(i,end=" ")

        if (value/i!=i):
            divisors.append(int(value/i))

divisors.sort()
print(*divisors,end=" ")

