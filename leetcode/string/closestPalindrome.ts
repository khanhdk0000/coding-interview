function nearestPalindromic(n: string): string {
  // <= 10, or 100, 1000 ...
  if (
    n.length === 1 ||
    (parseInt(n) % 10 === 0 &&
      n
        .split("")
        .slice(1)
        .every((d) => d === "0") &&
      n[0] === "1")
  ) {
    return (parseInt(n) - 1).toString();
  }
  // 11, 101, 1001 ...
  if (
    n === "11" ||
    (parseInt(n) % 10 === 1 &&
      n
        .split("")
        .slice(1, -1)
        .every((d) => d === "0"))
  ) {
    return (parseInt(n) - 2).toString();
  }
  // 99, 999, 9999 ...
  if (n.split("").every((d) => d === "9") && n.length > 1) {
    return (parseInt(n) + 2).toString();
  }

  const isEven = n.length % 2 === 0;
  const endIndexBase = isEven ? n.length / 2 : Math.floor(n.length / 2) + 1;
  const palidromeBase = n.slice(0, endIndexBase);
  const isPalindrome = buildPalindrome(palidromeBase, isEven) === n;
  const candidates = isPalindrome
    ? [
        buildPalindrome((parseInt(palidromeBase) - 1).toString(), isEven),
        buildPalindrome((parseInt(palidromeBase) + 1).toString(), isEven),
      ]
    : [
        buildPalindrome((parseInt(palidromeBase) - 1).toString(), isEven),
        buildPalindrome(palidromeBase, isEven),
        buildPalindrome((parseInt(palidromeBase) + 1).toString(), isEven),
      ];
  const diff = candidates.map((candidate) =>
    Math.abs(parseInt(candidate) - parseInt(n))
  );
  const minCandidate = candidates[diff.indexOf(Math.min(...diff))];
  return minCandidate;
}

function buildPalindrome(base: string, isEven: boolean): string {
  if (isEven) {
    return base + base.split("").reverse().join("");
  }
  return base + base.split("").reverse().slice(1).join("");
}
