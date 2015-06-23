class Prime_Number:
    """docstring for """
    def __init__(self, n):
        self.__sieve_ary = [];
        for i in range(n + 1):
            self.__sieve_ary.append(True)

        self.__sieve_ary[:2] = [False, False]

        for i in range(len(self.__sieve_ary)):
            if not self.__sieve_ary[i]:
                continue

            j = 2
            while i * j <= n:
                self.__sieve_ary[i * j] = False
                j += 1


        self.prime_ary = []
        for i in range(len(self.__sieve_ary)):
            if self.__sieve_ary[i]:
                self.prime_ary.append(i)


def term(n, prime_ary):
    a_n = prime_ary[n - 1] / (n ** 3)
    return a_n



prime_number = Prime_Number(10000000)
pary = prime_number.prime_ary

a = 0.0

for n in range(1, len(pary) + 1):
    a += term(n, pary)


print(a)
