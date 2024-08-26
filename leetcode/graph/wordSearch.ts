function exist(board: string[][], word: string): boolean {
  const rows = board.length;
  const m = board.length;
  const n = board[0].length;

  const backtrack = (i: number, j: number, k: number) => {
    if (k === word.length) {
      return true;
    }
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== word.charAt(k)) {
      return false;
    }

    const temp = board[i][j];
    board[i][j] = "\0";

    const result =
      backtrack(i + 1, j, k + 1) ||
      backtrack(i - 1, j, k + 1) ||
      backtrack(i, j + 1, k + 1) ||
      backtrack(i, j - 1, k + 1);

    board[i][j] = temp;
    return result;
  };

  for (let i = 0; i < m; ++i) {
    for (let j = 0; j < n; ++j) {
      if (backtrack(i, j, 0)) {
        return true;
      }
    }
  }
  return false;
}
