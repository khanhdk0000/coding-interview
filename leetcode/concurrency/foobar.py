import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.sem1 = threading.Semaphore(0)
        self.sem2 = threading.Semaphore(1)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            self.sem2.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sem1.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.sem1.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sem2.release()