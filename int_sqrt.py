def bin_search(arr,l,r,x):
    if l>r:
        return l-1
    m = (l+r) // 2

    if (arr[m] * arr[m] == x):
        return m
    elif (arr[m] * arr[m] > x ):
        return bin_search(arr , l , m-1 ,x )
    else :
        return bin_search(arr , m+1 , r ,x )

x = int(input("Enter number: "))
if x == 0 or x==1 :
        print(f"\nsqrt of {x} is {x}\n")
r = int(x/2)
arr = list()
for i in range(r):
    arr.append(i+1)


m = bin_search(arr , 0 , len(arr)-1 , x )
if x >= 2 :
    print(f"\nsqrt of {x} is {arr[m]}\n")
elif x < 0 :
    print("Enter Positive Integer Number.")


