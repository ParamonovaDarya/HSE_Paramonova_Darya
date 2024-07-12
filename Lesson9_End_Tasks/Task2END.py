...
Задание 2
Римские числа представлены семью разными символами: I, V, X, L, C, D, M.
Символ Значение
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
Примеры:
2 записывают как II, когда две единицы подставляют друг к другу;
12 записывают как XII, т.е. X + II;
Число 27 записывают как XXVII, т.е. XX + V + II.
Римские числа записывают обычно от большого к малому слева направо. Однако для
обозначения числа 4 не будет использоваться запись IIII. Вместо этого число 4
записывают как IV. Так как I идет перед V, оно вычитается из него и образует число 4.
Есть 6 возможных вариаций для вычитаний:
I может быть помещён перед V (5) и X (10), чтобы образовать 4 и 9;
X может быть помещён перед L (50) и C (100), чтобы образовать 40 и 90;
C может быть помещён перед D (500) и M (1000) чтобы образовать 400 и 900.
Напишите функцию-конвертер из системы римских цифр в знакомую нам десятичную
целочисленную.
...

def romanToInt(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    explanation = []
    
    for char in reversed(s):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
            explanation.append(f"- {current_value} ({char})")
        else:
            total += current_value
            explanation.append(f"+ {current_value} ({char})")
        prev_value = current_value
    
    explanation.append(f"Total: {total}")
    explanation.reverse() 
    
    print("\n".join(explanation))
    return total
input_str = input("Введите римское число: ")
output = romanToInt(input_str)
print(f"Результат: {output}")
