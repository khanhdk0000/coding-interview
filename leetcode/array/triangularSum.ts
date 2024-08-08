function triangularSum(nums: number[]): number {
  let arr = [...nums];
  while (arr.length > 1) {
    let tempArr: number[] = [];
    for (let i = 0; i < arr.length; i++) {
      tempArr.push((arr[i] + arr[i + 1]) % 10);
    }
    // clear the arr
    console.log(tempArr);
    arr = [];
    arr = [...tempArr];
  }
  return arr[0];
}
