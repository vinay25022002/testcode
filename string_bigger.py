def my_function(x):
    return x[::-1]
def find_value(mytxt):
    count=0
    for x in mytxt:
        i=mytxt.index(x)
        y=ord(x)
        print(x,"\n",i,"\n",y,"\n",count)
        count+=ord(x)*(26^i)
    return(count)
z=input("Enter your string: ")
z1=input("Enter another string: ")
mytxt= list(my_function(z))
mytxt1= list(my_function(z1))
a=find_value(mytxt)
b=find_value(mytxt1)
if a<b:
    print("The value of",z1, "is greater")
else:
    print("The value of",z, "is greater")

