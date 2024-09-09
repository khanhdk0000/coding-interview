class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
  const matrix: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));

  let top = 0;
  let bottom = m - 1;
  let left = 0;
  let right = n - 1;
  let direction = 0; // 0: right, 1: down, 2: left, 3: up
  let current = head;

  while (top <= bottom && left <= right && current !== null) {
    if (direction === 0) {
      // Moving right
      for (let i = left; i <= right && current !== null; i++) {
        matrix[top][i] = current.val;
        current = current.next;
      }
      top++;
    } else if (direction === 1) {
      // Moving down
      for (let i = top; i <= bottom && current !== null; i++) {
        matrix[i][right] = current.val;
        current = current.next;
      }
      right--;
    } else if (direction === 2) {
      // Moving left
      for (let i = right; i >= left && current !== null; i--) {
        matrix[bottom][i] = current.val;
        current = current.next;
      }
      bottom--;
    } else if (direction === 3) {
      // Moving up
      for (let i = bottom; i >= top && current !== null; i--) {
        matrix[i][left] = current.val;
        current = current.next;
      }
      left++;
    }
    // Move to the next direction
    direction = (direction + 1) % 4;
  }
  return matrix;
}
