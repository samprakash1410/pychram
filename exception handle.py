try:
    num=9
    den=4
    result=num/den

except ZeroDivisionError:
    print("denominator cannot be zero")

else:
    print("division successful,result=",result)

