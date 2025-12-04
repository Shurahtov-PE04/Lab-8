def get_permutations(s):
    # Базовый случай: если строка пустая или из одного символа
    if len(s) <= 1:
        return [s]

    permutations = []

    for i in range(len(s)):
        # Берем текущий символ
        current_char = s[i]
        # Оставшаяся часть строки без текущего символа
        remaining_chars = s[:i] + s[i + 1:]

        # Рекурсивно получаем перестановки для оставшейся части
        for perm in get_permutations(remaining_chars):
            # Добавляем текущий символ в начало каждой перестановки
            permutations.append(current_char + perm)

    return permutations

result = get_permutations("qwe")
print(result)
print(f"Количество перестановок: {len(result)}\n")

result2 = get_permutations("qw")
print(result2)
print(f"Количество перестановок: {len(result2)}\n")

result3 = get_permutations("q")
print(result3)
print(f"Количество перестановок: {len(result3)}")