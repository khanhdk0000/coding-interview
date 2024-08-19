function numTeams(rating: number[]): number {
    const n = rating.length;
    let count = 0;

    const leftSmaller = new Array(n).fill(0);
    const rightGreater = new Array(n).fill(0);
    const leftGreater = new Array(n).fill(0);
    const rightSmaller = new Array(n).fill(0);

    // Count left smaller and left greater
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < j; i++) {
            if (rating[i] < rating[j]) {
                leftSmaller[j]++;
            }
            if (rating[i] > rating[j]) {
                leftGreater[j]++;
            }
        }
    }

    // Count right smaller and right greater
    for (let j = 0; j < n; j++) {
        for (let k = j + 1; k < n; k++) {
            if (rating[j] < rating[k]) {
                rightGreater[j]++;
            }
            if (rating[j] > rating[k]) {
                rightSmaller[j]++;
            }
        }
    }

    // Calculate the number of valid teams
    for (let i = 0; i < n; i++) {
        count += leftSmaller[i] * rightGreater[i] + leftGreater[i] * rightSmaller[i];
    }

    return count;
}