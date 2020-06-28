a=int(input("Enter Number of test cases"))
def findMin(V):
    Amount = [1, 2, 5, 10, 20, 50,
            100, 500, 2000]
    n = len(Amount)
    ans = []
    i = n - 1

    while (i >= 0):
        while (V >= Amount[i]):
            V -= Amount[i]
            ans.append(Amount[i])
        i -= 1

        for i in range(len(ans)):
            print(ans[i], end=" ")

if __name__ == '__main__':
    for i in range(1,a+1):
        n = int(input("Enter the Number\n"))
        print("Following is minimal number",
            "of change for", n, ": ", end="\n")
    for x in range(1,a+1):
        findMin(n)
