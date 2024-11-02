function minPerimeter(N: number): number {
    let minPerimeter = 0;
    for (let i = 1; i <= Math.sqrt(N); i++) {
        if (N % i === 0) {
            minPerimeter = i;
        }
    }
    return 2 * (minPerimeter + N / minPerimeter);
}