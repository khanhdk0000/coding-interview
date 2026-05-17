import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem_zero = threading.Semaphore(1)
        self.sem_even = threading.Semaphore(0)
        self.sem_odd = threading.Semaphore(0)
        self.total_evens = n // 2
        self.total_odds = n // 2 + n % 2

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(self.n):
            self.sem_zero.acquire()
            printNumber(0)
            if (i + 1) % 2 == 1:
                self.sem_odd.release()
            else:
                self.sem_even.release()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(self.total_evens):
            self.sem_even.acquire()
            printNumber((i + 1) * 2)
            self.sem_zero.release()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(self.total_odds):
            self.sem_odd.acquire()
            printNumber(i * 2 + 1)
            self.sem_zero.release()
