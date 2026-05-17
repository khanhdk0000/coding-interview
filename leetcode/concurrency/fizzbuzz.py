from threading import Semaphore


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.num = 1  # shared current number — all threads read this
        self.sem_number = Semaphore(1)  # number goes first (1 is plain)
        self.sem_fizz = Semaphore(0)
        self.sem_buzz = Semaphore(0)
        self.sem_fizzbuzz = Semaphore(0)

    def _advance(self):
        """Increment shared counter and wake whichever thread handles the next number."""
        self.num += 1
        self._signal(self.num)

    def _signal(self, i):
        """Release the semaphore for whoever owns number i.
        If i > n, release ALL four semaphores so every thread can wake up,
        see num > n, and exit cleanly — avoiding deadlock."""
        if i > self.n:
            self.sem_fizz.release()
            self.sem_buzz.release()
            self.sem_fizzbuzz.release()
            self.sem_number.release()
        elif i % 15 == 0:
            self.sem_fizzbuzz.release()
        elif i % 3 == 0:
            self.sem_fizz.release()
        elif i % 5 == 0:
            self.sem_buzz.release()
        else:
            self.sem_number.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: "Callable[[], None]") -> None:
        while True:
            self.sem_fizz.acquire()
            if self.num > self.n:
                return  # exit token received
            printFizz()
            self._advance()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        while True:
            self.sem_buzz.acquire()
            if self.num > self.n:
                return
            printBuzz()
            self._advance()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        while True:
            self.sem_fizzbuzz.acquire()
            if self.num > self.n:
                return
            printFizzBuzz()
            self._advance()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: "Callable[[int], None]") -> None:
        while True:
            self.sem_number.acquire()
            if self.num > self.n:
                return
            printNumber(self.num)  # self.num is the real current number
            self._advance()
