// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function binaryGap(N: number): number {
    // Implement your solution here
    const binaryString = N.toString(2);
    let maxGap = 0;
    let currentGap = 0;
    let foundOne = false;
    for (const c of binaryString) {
        if (c === "1") {
            if (foundOne) {
                maxGap = Math.max(maxGap, currentGap);
                currentGap = 0;
            }
            foundOne = true;
        } else {
            currentGap += 1;
        }
    }
    return maxGap;
}
