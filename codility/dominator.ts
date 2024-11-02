function dominator(A: number[]): number {
    const n = A.length;
    const stack: number[] = [];
    
    for (let i = 0; i < n; i++) {
        if (stack.length === 0) {
            stack.push(A[i]);
        } else {
            if (stack[stack.length - 1] !== A[i]) {
                stack.pop();
            } else {
                stack.push(A[i]);
            }
        }
    }
    
    if (stack.length === 0) {
        return -1;
    }
    
    const candidate = stack[0];
    let count = 0;
    let index = -1;
    
    for (let i = 0; i < n; i++) {
        if (A[i] === candidate) {
            count++;
            index = i;
        }
    }
    
    return count > n / 2 ? index : -1;
}