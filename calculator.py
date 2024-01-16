def main(input_str):
    try:
        prisvoenie = input_str.split()
        a = int(prisvoenie[0])
        d = prisvoenie[1]
        b = int(prisvoenie[2])
        if len(prisvoenie) != 3:
            raise ValueError()
        if d not in ['-','+','*','/']:
            raise ValueError()
        if 1 <= a <= 10 and 1 <= b <= 10:
            if d == '+':
                result = a+b
            elif d == '-':
                result = a-b
            elif d == '*':
                result = a*b
            elif d == '/':
                result = a//b
        else:
            raise ValueError()
        return result
    except:
        raise ValueError()


input_str = input("Введите выражение (пример: 5 + 2): ")
try:
    result = main(input_str)
    print("Результат:",result)
except:
    print("Неверный ввод!")







