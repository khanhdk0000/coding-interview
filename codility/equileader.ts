function equiLeader(A: number[]): number {
    const n = A.length;
    
    // Step 1: Find the candidate for the leader using Boyer-Moore Voting Algorithm
    let candidate = -1;
    let count = 0;
    for (const num of A) {
        if (count === 0) {
            candidate = num;
            count = 1;
        } else if (num === candidate) {
            count++;
        } else {
            count--;
        }
    }
    
    // Step 2: Verify that the candidate is actually the leader
    let leaderCount = 0;
    for (const num of A) {
        if (num === candidate) leaderCount++;
    }
    
    // If the candidate isn't the leader, there are no equi leaders
    if (leaderCount <= n / 2) return 0;
    
    const leader = candidate;
    let equiLeaders = 0;
    let leftLeaderCount = 0;
    
    // Step 3: Count equi leaders by iterating through possible split points
    for (let i = 0; i < n - 1; i++) {
        if (A[i] === leader) leftLeaderCount++;
        
        const leftSize = i + 1;
        const rightSize = n - leftSize;
        
        // Check if leader is the leader in both the left and right parts
        if (leftLeaderCount > leftSize / 2 && (leaderCount - leftLeaderCount) > rightSize / 2) {
            equiLeaders++;
        }
    }
    
    return equiLeaders;
}
