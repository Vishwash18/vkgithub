#Coin Distribution problem

value=int(input())

#checking for five rupees
five=int((value-4)/5)

#checking for one rupee
one=(value-(5*five))
if one%2==0:
    one=2
else:
    one=1

#Checking foe two rupees
two=int((value-(5*five)-(1*one))/2)

print(five+one+two,"\n",five,one,two)