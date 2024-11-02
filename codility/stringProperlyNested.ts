function stringProperlyNested(S: string): number {
  const stack: string[] = [];
  for (let i = 0; i < S.length; i++) {
    const char = S[i];
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else {
      const last = stack.pop();
      if (last === undefined) return 0;
      if (char === ")" && last !== "(") return 0;
      if (char === "]" && last !== "[") return 0;
      if (char === "}" && last !== "{") return 0;
    }
  }
  return stack.length === 0 ? 1 : 0;
}
