function digitSum(s: string, k: number): string {
  let res = s;
  while (res.length > k) {
    let newStr = "";
    let i = 0;
    let j = k;
    while (i < res.length) {
      if (j > res.length) {
        j = res.length;
      } 
      const subStr = res.slice(i, j);
      const total = subStr
        .split("")
        .reduce((acc, curr) => acc + parseInt(curr), 0);
      newStr += total.toString();
      i += k;
      j += k;
    }
    res = newStr;
  }
  return res;
}
