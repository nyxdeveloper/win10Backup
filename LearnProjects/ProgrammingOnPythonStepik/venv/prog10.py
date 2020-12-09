# поиск числа фибоначи по его номеру

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(int(input('Введите номер '))))
