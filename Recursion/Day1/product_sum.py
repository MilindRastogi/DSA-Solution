def Product_Sum(arr, depth=1):
    sum = 0
    for i in arr:
        if isinstance(i, list):
            sum = sum + Product_Sum(i, depth+1)
        else:
            sum = sum + i
    return sum*depth


arr = [1, 2, [3, 4]]
print(Product_Sum(arr))
