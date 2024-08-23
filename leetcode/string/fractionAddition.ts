function GCD(a: number, b: number): number {
  return b ? GCD(b, a % b) : Math.abs(a);
}

function fractionAddition(expression: string): string {
  const fractions = expression.match(/[+-]?\d+\/\d+/g) || [];
  let [numerator, denominator] = [0, 1];
  for (let fraction of fractions) {
    const [num, den] = fraction.split("/").map(Number);
    numerator = numerator * den + num * denominator;
    denominator *= den;
    const gcd = GCD(numerator, denominator);
    numerator /= gcd;
    denominator /= gcd;
  }
  return `${numerator}/${denominator}`;
}
