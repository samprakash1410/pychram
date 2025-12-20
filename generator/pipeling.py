def fibonacii_series(nums):
    x,z=0,4
    for i in range(nums):
        x,z=z,x+z
        yield x


def square(nums):
    for num in nums:
        yield num**2


print(sum(square(fibonacii_series(7))))

