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