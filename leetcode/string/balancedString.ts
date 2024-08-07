function balancedString(s: string): number {
  const charCount = new Map<string, number>();
  for (const char of s) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }
  const target = s.length / 4;
  const excess = new Map<string, number>();
  for (const [char, count] of charCount) {
    if (count > target) {
      excess.set(char, count - target);
    }
  }
  if (excess.size === 0) {
    return 0;
  }
  // Sliding window to find the smallest substring that contains all excess characters
  let minLen = s.length;
  let left = 0;
  let right = 0;
  let missing = excess.size;
  while (right < s.length) {
    const char = s[right];
    if (excess.has(char)) {
      excess.set(char, (excess.get(char) as number) - 1);
      if (excess.get(char) === 0) {
        missing--;
      }
    }
    while (missing === 0) {
      minLen = Math.min(minLen, right - left + 1);
      const leftChar = s[left];
      if (excess.has(leftChar)) {
        excess.set(leftChar, (excess.get(leftChar) as number) + 1);
        if ((excess.get(leftChar) as number) > 0) {
          missing++;
        }
      }
      left++;
    }
    right++;
  }
  return minLen;
}
