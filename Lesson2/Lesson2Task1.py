def factorial():
    a = int(input())
    f = 1
    for i in range (a + 1):
        if i == 0:
            continue
        else:
            f = f * i
    return (f)
print(factorial())