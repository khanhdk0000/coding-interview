function maxDistance(arrays: number[][]): number {
    let min = arrays[0][0];
    let max = arrays[0][arrays[0].length - 1];
    let indexMax = 0;
    for (let i = 1; i < arrays.length; i++) {
        min = Math.min(min, arrays[i][0]);
        max = Math.max(max, arrays[i][arrays[i].length - 1]);
        indexMax = arrays[i][arrays[i].length - 1] > arrays[indexMax][arrays[indexMax].length - 1] ? i : indexMax;
    }
    if (arrays[indexMax][0] === min) {
        // Find second min
        let secondMin = 0;
        let secondMax = 0;
        if (indexMax === 0) {
            secondMin = arrays[1][0];
            secondMax = arrays[1][arrays[1].length - 1];
        } else {
            secondMin = arrays[0][0];
            secondMax = arrays[0][arrays[0].length - 1];
        }
        for (let i = 0; i < arrays.length; i++) {
            if (i !== indexMax) {
                secondMin = Math.min(secondMin, arrays[i][0]);
                secondMax = Math.max(secondMax, arrays[i][arrays[i].length - 1]);
            }
        }
        return Math.max(max - secondMin, secondMax - min);
    }
    return max - min;
};