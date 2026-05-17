import threading


class H2O:
    def __init__(self):
        self.sem_hydrogen = threading.Semaphore(2)
        self.sem_oxygen = threading.Semaphore(1)
        # action= is called ONCE when all 3 parties arrive, before any are released.
        # This is the perfect place to reset semaphores for the next molecule.
        self.barrier = threading.Barrier(3, action=self._reset)

    def _reset(self):
        # Restore exactly 2 hydrogen slots and 1 oxygen slot for the next molecule.
        # Called atomically by the barrier — no race condition possible.
        self.sem_hydrogen.release()
        self.sem_hydrogen.release()
        self.sem_oxygen.release()

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        # Block until a hydrogen slot is available (max 2 per molecule)
        self.sem_hydrogen.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        # Wait for the other 2 atoms (1H + 1O) to also finish printing.
        # Once all 3 arrive, _reset() runs and everyone is released together.
        self.barrier.wait()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        # Block until the oxygen slot is available (max 1 per molecule)
        self.sem_oxygen.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        # Wait for the other 2 atoms (2H) to also finish printing.
        self.barrier.wait()
