n=int(input("enter the number:"))
if n>0:
    print("positive",end="")
    if n%2==0:  
        print(" even number")
    else:
        print(" odd number")
elif n<0:
    print("negative",end="")
    if n%2==0:
        print(" even number")
    else:
        print(" odd number")
else:
    print("zero")   
# The above code checks if a number is positive, negative, or zero.
