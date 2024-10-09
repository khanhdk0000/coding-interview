function minAddToMakeValid(s: string): number {
  let stack: string[] = [];
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(s[i]);
    } else {
      if (stack.length === 0) {
        count++;
      } else {
        stack.pop();
      }
    }
  }
  return count + stack.length;
}
