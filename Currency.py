#To find minimum number of currency to buy a product at a range of 5000

a=int(input("Enter no of Test Cases"))
def findMin(V):
    #Indian Currency
    Currency= [1, 2, 5, 10, 20, 50,
            100, 500, 2000]
    n = len(Currency)
    ans = []

    i = n - 1
    while (i >= 0):


        while (V >= Currency[i]):
            V -= Currency[i]
            ans.append(Currency[i])
        i -= 1

    for i in range(len(ans)):
        print(ans[i], end=" ")


for x in range(1,a+1):
    if __name__ == '__main__':
        n = int(input("\nEnter the Number:"))
        print("Following is minimal number",
              "of change for", n, ": ", end="\n")
        findMin(n)
