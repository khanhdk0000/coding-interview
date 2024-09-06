class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const numMap = new Map<number, boolean>();
    for(let num of nums) {
        numMap.set(num, true);
    }
    // iterative approach
    let dummy = new ListNode(0);
    dummy.next = head;
    let current = dummy;
    while(current.next) {
        if(numMap.has(current.next.val)) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return dummy.next;
}
