import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return quicksort(less) + equal + quicksort(greater)


length = random.randint(5, 10)  # 要素数は5から10の範囲でランダムに生成
array = [random.randint(1, 100) for _ in range(length)]  

print("ソート前:", array)
sorted_array = quicksort(array)
print("ソート後:", sorted_array)
