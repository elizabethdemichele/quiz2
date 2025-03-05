def es_primo(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

def es_deficiente(n):
    suma = 1
    for i in range(2, n - 1):
        if n % i == 0:
            suma += i
    if suma < n:
        return True
    return False
