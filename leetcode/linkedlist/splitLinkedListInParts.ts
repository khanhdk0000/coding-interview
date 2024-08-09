class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function splitListToParts(
  head: ListNode | null,
  k: number
): Array<ListNode | null> {
  let len = 0;
  let temp = head;
  while (temp) {
    len++;
    temp = temp.next;
  }

  let width = Math.floor(len / k);
  let remainder = len % k;

  let result = new Array(k).fill(null);

  let current = head;
  for (let i = 0; i < k; i++) {
    let head = current;
    for (let j = 0; j < width + (i < remainder ? 1 : 0) - 1; j++) {
      if (current) {
        current = current.next;
      }
    }
    if (current) {
      let prev = current;
      current = current.next;
      prev.next = null;
    }
    result[i] = head;
  }

  return result;
}
