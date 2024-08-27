function maxProbability(n: number, edges: number[][], succProb: number[], start: number, end: number): number {
    // Build the graph using an adjacency list
    const graph: Map<number, Array<[number, number]>> = new Map();
    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        const prob = succProb[i];
        
        if (!graph.has(u)) graph.set(u, []);
        if (!graph.has(v)) graph.set(v, []);
        
        graph.get(u)!.push([v, prob]);
        graph.get(v)!.push([u, prob]);
    }

    // Array to keep track of the best probability found so far to each node
    const probabilities = new Array(n).fill(0);
    probabilities[start] = 1;  // Start node has a probability of 1 to reach itself

    // Array to simulate the priority queue (node index, probability)
    const pq: { node: number, prob: number }[] = [];
    pq.push({ node: start, prob: 1 });

    while (pq.length > 0) {
        // Find the node with the maximum probability
        let maxIndex = 0;
        for (let i = 1; i < pq.length; i++) {
            if (pq[i].prob > pq[maxIndex].prob) {
                maxIndex = i;
            }
        }
        const { node, prob } = pq.splice(maxIndex, 1)[0];

        // Early exit if the end node is reached
        if (node === end) return prob;

        // Process all adjacent nodes
        if (graph.has(node)) {
            for (const [neighbor, edgeProb] of graph.get(node)!) {
                const newProb = prob * edgeProb;
                if (newProb > probabilities[neighbor]) {
                    probabilities[neighbor] = newProb;
                    pq.push({ node: neighbor, prob: newProb });
                }
            }
        }
    }

    // If the end node is never reached, return 0
    return 0;
}
