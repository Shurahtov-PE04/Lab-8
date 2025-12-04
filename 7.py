def find_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        # Рекурсивно находим максимум в оставшейся части массива
        max_rest = find_max(arr[1:])
        # Сравниваем первый элемент с максимумом оставшейся части
        return arr[0] if arr[0] > max_rest else max_rest

print(find_max([92, 2, 1, 3, 91, 4, 5]))
print(find_max([-2, -19, -10]))
print(find_max([90]))                       
print(find_max([]))

