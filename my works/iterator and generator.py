import time


class PrimeNumbers:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 0:
            if self.i > self.n:
                raise StopIteration()
            return self.i


started_at = time.time()

prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


def prime_numbers_generator(n):
    for i in range(1, n + 1):
        yield i


for number in prime_numbers_generator(n=10000):
    print(number)

ended_at = time.time()
diff_time = ended_at - started_at
print(round(diff_time, 4), 'sec')
