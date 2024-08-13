function combinationSum2(candidates: number[], target: number): number[][] {
    const res: number[][] = [];
    const path: number[] = [];
    candidates.sort((a, b) => a - b);
    dfs(candidates, target, 0, path, res);
    return res;
};

function dfs(candidates: number[], target: number, start: number, path: number[], res: number[][]) {
    if (target === 0) {
        res.push([...path]);
        return;
    }
    for (let i = start; i < candidates.length; i++) {
        if (i > start && candidates[i] === candidates[i - 1]) {
            continue;
        }
        if (candidates[i] > target) {
            break;
        }
        path.push(candidates[i]);
        dfs(candidates, target - candidates[i], i + 1, path, res);
        path.pop();
    }
}