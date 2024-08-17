function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const map = new Map<number, number>();
    const result: number[] = [];
    const notInArr2: number[] = [];
    for (let i = 0; i < arr2.length; i++) {
        map.set(arr2[i], 0);
    }
    for (let i = 0; i < arr1.length; i++) {
        if (map.has(arr1[i])) {
            map.set(arr1[i], map.get(arr1[i])! + 1);
        } else {
            notInArr2.push(arr1[i]);
        }
    }
    notInArr2.sort((a, b) => a - b);
    for (let i = 0; i < arr2.length; i++) {
        for (let j = 0; j < map.get(arr2[i])!; j++) {
            result.push(arr2[i]);
        }
    }
    result.push(...notInArr2);
    return result;
};