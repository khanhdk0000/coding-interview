function distinceValue(A: number[]): number {
    const n = A.length;
    const set = new Set<number>();
    
    for (let i = 0; i < n; i++) {
        set.add(A[i]);
    }
    
    return set.size;
}