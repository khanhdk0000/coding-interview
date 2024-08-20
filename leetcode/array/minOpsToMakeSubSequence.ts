function minOperations(target: number[], arr: number[]): number {
  const map = new Map<number, number>();
  for (let i = 0; i < target.length; i++) {
    map.set(target[i], i);
  }
  const stack: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i])) {
      stack.push(map.get(arr[i]) as number);
    }
  }
  // Find longest increasing subsequence
  const lis: number[] = [];
  for (const num of stack) {
    const index = binarySearch(lis, num);
    if (index === lis.length) {
      lis.push(num);
    } else {
      lis[index] = num;
    }
  }
  return target.length - lis.length;
}

function binarySearch(arr: number[], target: number): number {
  let low = 0;
  let high = arr.length;
  while (low < high) {
    const mid = low + Math.floor((high - low) / 2);
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid;
    }
  }
  return low;
}