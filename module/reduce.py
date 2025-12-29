from functools import reduce

a=[3,6,9,8]

res=reduce(lambda x,y:x+y,a,91)

print(res)