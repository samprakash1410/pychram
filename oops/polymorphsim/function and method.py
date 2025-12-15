def calculate_area(length,width=None):
    if width is None:
        return length * length
    return length * width

print(calculate_area(9))
print(calculate_area(9,4))

