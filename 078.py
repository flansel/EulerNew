# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
 
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
 
    return table
 
# Driver program to test above function
n = 100000
arr = [i for i in range(1,n)]
m = len(arr)
x = count(arr, m, n)
for i,y in enumerate(x):
    print(i,y)
    if y % 1000000 == 0:
        print(i,y)
        quit()
