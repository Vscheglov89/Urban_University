numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
for num in numbers:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        primes.append(num)
    else:
        not_primes.append(num)
print('Простые числа: ', primes)
print('Не простые числа  ', not_primes)