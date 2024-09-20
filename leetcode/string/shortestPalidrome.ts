
// KMP algorithm
function shortestPalindrome(s: string): string {
  let rev = s.split("").reverse().join("");
  let l = s + "#" + rev;
  let p = new Array(l.length).fill(0);
  for (let i = 1; i < l.length; i++) {
    let j = p[i - 1];
    while (j > 0 && l[i] !== l[j]) {
      j = p[j - 1];
    }
    if (l[i] === l[j]) {
      j++;
    }
    p[i] = j;
  }
  return rev.slice(0, s.length - p[l.length - 1]) + s;
}
