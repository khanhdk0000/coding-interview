function isBoomerang(points: number[][]): boolean {
    const [a, b, c] = points;
    // check if the slope of two lines are equal
    return (b[1] - a[1]) * (c[0] - b[0]) !== (c[1] - b[1]) * (b[0] - a[0]); 
};
