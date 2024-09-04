function robotSim(commands: number[], obstacles: number[][]): number {
  const set: Set<string> = new Set();
  for (let obs of obstacles) {
    set.add(`${obs[0]} ${obs[1]}`);
  }

  const dirs: number[][] = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  let d: number = 0;
  let x: number = 0;
  let y: number = 0;
  let result: number = 0;

  for (let c of commands) {
    if (c === -1) {
      d = (d + 1) % 4;
    } else if (c === -2) {
      d = (d - 1 + 4) % 4;
    } else {
      while (c-- > 0 && !set.has(`${x + dirs[d][0]} ${y + dirs[d][1]}`)) {
        x += dirs[d][0];
        y += dirs[d][1];
      }
    }
    result = Math.max(result, x * x + y * y);
  }

  return result;
}
