class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.last_num = 1
        self.prime_numbers = []

    def __iter__(self):
        self.last_num = 1
        return self

    def __next__(self):
        for num in range(self.last_num + 1, self.n + 1):
            for prime in self.prime_numbers:
                if num % prime == 0:
                    break
            else:
                self.last_num = num
                self.prime_numbers.append(num)
                return num
        raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


fff = get_prime_numbers(5555)
for num in fff:
    print(num)


