function diffWaysToCompute(expression: string): number[] {
  const result: number[] = [];
  for (let i = 0; i < expression.length; i++) {
    const c = expression[i];
    if (c === "+" || c === "-" || c === "*") {
      const left = diffWaysToCompute(expression.substring(0, i));
      const right = diffWaysToCompute(expression.substring(i + 1));
      for (const l of left) {
        for (const r of right) {
          if (c === "+") {
            result.push(l + r);
          } else if (c === "-") {
            result.push(l - r);
          } else {
            result.push(l * r);
          }
        }
      }
    }
  }
  if (result.length === 0) {
    result.push(parseInt(expression));
  }
  return result;
}
