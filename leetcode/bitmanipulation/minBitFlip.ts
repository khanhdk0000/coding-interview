function minBitFlips(start: number, goal: number): number {
  const startBinary = start.toString(2);
  const goalBinary = goal.toString(2);

  let longBinary = "";
  let shortBinary = "";
  if (startBinary.length > goalBinary.length) {
    longBinary = startBinary;
    shortBinary = goalBinary;
  } else {
    longBinary = goalBinary;
    shortBinary = startBinary;
  }
  let flips = 0;
  const reversedShortBinary = shortBinary.split("").reverse().join("");
  const reversedLongBinary = longBinary.split("").reverse().join("");

  for (let i = reversedShortBinary.length - 1; i >= 0; i--) {
    if (reversedShortBinary[i] !== reversedLongBinary[i]) {
      flips++;
    }
  }

  for (let i = reversedShortBinary.length; i < reversedLongBinary.length; i++) {
    if (reversedLongBinary[i] === "1") {
      flips++;
    }
  }

  return flips;
}
