function lastSubstring(s: string): string {
  let currentIdx = 0;
  let compareIdx = 1;
  let compareLength = 0;
  while (compareIdx + compareLength < s.length) {
    if (s[currentIdx + compareLength] === s[compareIdx + compareLength]) {
      compareLength++;
    } else if (s[currentIdx + compareLength] < s[compareIdx + compareLength]) {
      currentIdx = Math.max(currentIdx + compareLength + 1, compareIdx);
      compareIdx = currentIdx + 1;
      compareLength = 0;
    } else {
      compareIdx = compareIdx + compareLength + 1;
      compareLength = 0;
    }
  }
  return s.slice(currentIdx);
}
