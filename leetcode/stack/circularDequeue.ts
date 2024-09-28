class MyCircularDeque {
  private deque: number[];
  private maxSize: number;

  constructor(k: number) {
    this.deque = [];
    this.maxSize = k;
  }

  // Insert an element at the front. Return true if the operation is successful, false if full.
  insertFront(value: number): boolean {
    if (this.isFull()) {
      return false;
    }
    this.deque.unshift(value);
    return true;
  }

  // Insert an element at the rear. Return true if the operation is successful, false if full.
  insertLast(value: number): boolean {
    if (this.isFull()) {
      return false;
    }
    this.deque.push(value);
    return true;
  }

  // Delete an element from the front. Return true if the operation is successful, false if empty.
  deleteFront(): boolean {
    if (this.isEmpty()) {
      return false;
    }
    this.deque.shift();
    return true;
  }

  // Delete an element from the rear. Return true if the operation is successful, false if empty.
  deleteLast(): boolean {
    if (this.isEmpty()) {
      return false;
    }
    this.deque.pop();
    return true;
  }

  // Get the front element. Return -1 if the deque is empty.
  getFront(): number {
    return this.isEmpty() ? -1 : this.deque[0];
  }

  // Get the last element. Return -1 if the deque is empty.
  getRear(): number {
    return this.isEmpty() ? -1 : this.deque[this.deque.length - 1];
  }

  // Check if the deque is empty.
  isEmpty(): boolean {
    return this.deque.length === 0;
  }

  // Check if the deque is full.
  isFull(): boolean {
    return this.deque.length === this.maxSize;
  }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
