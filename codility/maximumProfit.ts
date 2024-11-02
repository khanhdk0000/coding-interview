function maximumProfit(A: number[]): number {
    const n = A.length;
    let maxProfit = 0;
    let minPrice = Infinity;
    
    for (let i = 0; i < n; i++) {
        minPrice = Math.min(minPrice, A[i]);
        maxProfit = Math.max(maxProfit, A[i] - minPrice);
    }
    
    return maxProfit;
}
